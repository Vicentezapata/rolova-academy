import { NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';
import { execFile } from 'child_process';
import util from 'util';
import { GoogleGenAI } from '@google/genai';
import { COURSES_ROOT, realPathInsideRoot, toFileApiUrl } from '@/app/lib/safePath';

const execFilePromise = util.promisify(execFile);

const SKILL_ROOT = path.join(process.cwd(), '.agents', 'skills', 'eva-presentation-generator');
const THEME_ID = /^[a-z0-9_]{1,40}$/;
const MAX_INGESTED_CHARS = 30000;

async function isKnownTheme(theme) {
  if (typeof theme !== 'string' || !THEME_ID.test(theme) || theme.startsWith('_')) return false;
  try {
    const stat = await fs.stat(path.join(SKILL_ROOT, 'theme-packs', theme));
    return stat.isDirectory();
  } catch {
    return false;
  }
}

export async function POST(req) {
  try {
    const body = await req.json();
    const { topic, selectedCourse, selectedUnit, theme, investigate } = body;

    if (typeof topic !== 'string' || topic.trim().length === 0) {
      return NextResponse.json({ error: 'Debes indicar un tema.' }, { status: 400 });
    }
    if (!(await isKnownTheme(theme))) {
      return NextResponse.json({ error: 'Tema no válido.' }, { status: 400 });
    }
    if (!selectedCourse || !selectedUnit) {
      return NextResponse.json({ error: 'Debes seleccionar un curso y una unidad.' }, { status: 400 });
    }

    // La unidad debe existir y estar contenida en cursos/
    const unitDir = await realPathInsideRoot(COURSES_ROOT, selectedCourse, selectedUnit);
    if (!unitDir) {
      return NextResponse.json({ error: 'Curso o unidad no válidos.' }, { status: 400 });
    }

    console.log('Iniciando generación para:', topic);

    // 1. Ingesta: leer los documentos de material/ (opcional)
    let ingestedText = 'Sin material base proveído.';
    const materialPath = await realPathInsideRoot(unitDir, 'material');
    if (materialPath) {
      const entries = await fs.readdir(materialPath, { withFileTypes: true });
      const chunks = [];
      for (const entry of entries) {
        if (!entry.isFile()) continue;
        if (!/\.(md|txt)$/i.test(entry.name)) continue;
        const content = await fs.readFile(path.join(materialPath, entry.name), 'utf-8');
        chunks.push(`\n\n--- Archivo: ${entry.name} ---\n${content}`);
      }
      if (chunks.length > 0) ingestedText = chunks.join('');
    }

    // 2. Cerebro (LLM): Generar el visual_plan.json
    const apiKey = process.env.GEMINI_API_KEY;
    if (!apiKey || apiKey === 'tu_api_key_aqui_por_favor') {
      return NextResponse.json({ error: "Falta configurar GEMINI_API_KEY en .env.local" }, { status: 500 });
    }

    const ai = new GoogleGenAI({ apiKey });
    
    const systemPrompt = `Eres un Director de Arte de Presentaciones Educativas.
Tu trabajo es generar un visual_plan.json estricto para crear una presentación en HTML.
Tema: ${topic}
Investigar y expandir: ${investigate ? 'Sí' : 'No'}

Reglas de Diseño:
- Debes devolver UNICAMENTE un objeto JSON válido (sin Markdown de código alrededor, solo el JSON raw).
- Usa los siguientes templates_html: cover.html, toc.html, section-divider.html, bullets.html, two-column.html, three-column.html, comparison.html, timeline.html, kpi-grid.html, stat-highlight.html, big-quote.html, image-hero.html, matrix-chart.html, thanks.html.
- Cada slide debe tener: "template_html", "title" y los placeholders requeridos por el template (ej. "text", "bullets": [], "stats": [[valor, label]], "q1_title", etc).
- Para estructurar, usa "part_label" (ej. "01 CONCEPTOS") en las slides de contenido.
- Usa "decoration_hints": ["W1"] para títulos con gradiente, ["W2"] para tarjetas cortadas, ["W3"] para efecto de luz de fondo, ["W7"] para tarjetas de cristal.

Esquema JSON requerido:
{
  "theme": "${theme}",
  "title": "${topic}",
  "slides": [
    { "template_html": "cover.html", "title": "...", "text": "...", "decoration_hints": ["W1"] },
    ...
  ]
}`;

    const prompt = `Por favor, genera el plan visual para la presentación en formato JSON.
Material base extraído:
${ingestedText.substring(0, MAX_INGESTED_CHARS)}
`;

    const modelToUse = process.env.GEMINI_MODEL || 'gemini-2.5-pro';
    console.log(`Llamando a Gemini API (Modelo: ${modelToUse})...`);
    
    const response = await ai.models.generateContent({
      model: modelToUse,
      contents: [
        { role: 'user', parts: [{ text: systemPrompt + "\n\n" + prompt }] }
      ],
      config: {
        responseMimeType: 'application/json',
      }
    });

    const jsonString = response.text;
    if (!jsonString) {
      return NextResponse.json({ error: 'El modelo no devolvió contenido.' }, { status: 502 });
    }
    try {
      JSON.parse(jsonString);
    } catch {
      return NextResponse.json({ error: 'El modelo devolvió un JSON no válido.' }, { status: 502 });
    }

    // 3. Músculo (Python): Guardar JSON y ejecutar ensamblador
    const planPath = path.join(unitDir, 'visual_plan.json');
    await fs.writeFile(planPath, jsonString, 'utf-8');
    
    console.log(`Plan visual guardado en: ${planPath}`);
    console.log("Ejecutando ensamblador Python...");
    
    const pythonScriptPath = path.join(SKILL_ROOT, 'scripts', 'generate_presentation_template.py');

    try {
      await fs.access(pythonScriptPath);
    } catch {
      return NextResponse.json({ error: `No se encontró el script de Python en ${pythonScriptPath}` }, { status: 500 });
    }

    // execFile sin shell: los argumentos nunca se interpretan como comandos
    const { stdout, stderr } = await execFilePromise(
      process.env.PYTHON_BIN || 'python3',
      [pythonScriptPath, '--unit-path', unitDir, '--pack', theme],
      { timeout: 120000, maxBuffer: 10 * 1024 * 1024 }
    );
    
    console.log("Resultado de Python:", stdout);
    if (stderr) console.warn("Advertencia de Python:", stderr);

    const previewPath = path.join(unitDir, 'presentation', 'preview.html');
    try {
      await fs.access(previewPath);
    } catch {
      return NextResponse.json({ error: 'El ensamblador no generó preview.html.' }, { status: 500 });
    }

    return NextResponse.json({ 
        success: true, 
        message: "Presentación generada con éxito.",
        presentationPath: path.relative(COURSES_ROOT, path.dirname(previewPath)),
        previewUrl: toFileApiUrl(previewPath)
    });

  } catch (error) {
    console.error("Error en generación:", error);
    return NextResponse.json({ error: error.message || "Error interno del servidor" }, { status: 500 });
  }
}
