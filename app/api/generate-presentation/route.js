import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';
import { exec } from 'child_process';
import util from 'util';
import { GoogleGenAI } from '@google/genai';

const execPromise = util.promisify(exec);

export async function POST(req) {
  try {
    const body = await req.json();
    const { topic, selectedCourse, selectedUnit, theme, mode, investigate } = body;

    console.log("Iniciando generación para:", topic);
    
    // Construir la ruta absoluta basada en el portal
    let materialPath = null;
    if (selectedCourse && selectedUnit) {
      materialPath = path.join(process.cwd(), 'cursos', selectedCourse, selectedUnit, 'material');
    }

    // 1. Ingesta: Leer los documentos de la ruta
    let ingestedText = "";
    let unitDir = "";
    
    if (materialPath && fs.existsSync(materialPath)) {
      const isDir = fs.lstatSync(materialPath).isDirectory();
      if (isDir) {
        // Encontrar archivos .md, .txt, etc.
        const files = fs.readdirSync(materialPath);
        for (const file of files) {
          if (file.endsWith('.md') || file.endsWith('.txt')) {
            const filePath = path.join(materialPath, file);
            ingestedText += `\n\n--- Archivo: ${file} ---\n`;
            ingestedText += fs.readFileSync(filePath, 'utf-8');
          }
        }
        unitDir = path.dirname(materialPath); // El directorio padre (ej: UNIDAD 3)
      } else {
        ingestedText = fs.readFileSync(materialPath, 'utf-8');
        unitDir = path.dirname(path.dirname(materialPath));
      }
    } else {
      console.log("Ruta no válida o vacía. Usando solo el tema.");
      ingestedText = "Sin material base proveído.";
      // Si no hay ruta, crearemos un temp dir en el portal
      unitDir = path.join(process.cwd(), 'public', 'temp_presentation');
      if (!fs.existsSync(unitDir)) fs.mkdirSync(unitDir, { recursive: true });
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
${ingestedText.substring(0, 30000)} // Truncado para no exceder límites si es muy largo
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

    let jsonString = response.text;
    
    // 3. Músculo (Python): Guardar JSON y ejecutar ensamblador
    const planPath = path.join(unitDir, 'visual_plan.json');
    fs.writeFileSync(planPath, jsonString, 'utf-8');
    
    console.log(`Plan visual guardado en: ${planPath}`);
    console.log("Ejecutando ensamblador Python...");
    
    // Ruta absoluta del script Python (que vive en .agents/...)
    // Asumiendo que academy-portal está al mismo nivel que .agents
    const pythonScriptPath = path.join(process.cwd(), '..', '.agents', 'skills', 'eva-presentation-generator', 'scripts', 'generate_presentation_template.py');
    
    if (!fs.existsSync(pythonScriptPath)) {
        return NextResponse.json({ error: `No se encontró el script de Python en ${pythonScriptPath}` }, { status: 500 });
    }

    const cmd = `python "${pythonScriptPath}" --unit-path "${unitDir}" --theme "${theme}"`;
    const { stdout, stderr } = await execPromise(cmd);
    
    console.log("Resultado de Python:", stdout);
    if (stderr) console.warn("Advertencia de Python:", stderr);

    const presentationUrl = `file:///${path.join(unitDir, 'presentation', 'preview.html').replace(/\\/g, '/')}`;

    return NextResponse.json({ 
        success: true, 
        message: "Presentación generada con éxito.",
        presentationPath: path.join(unitDir, 'presentation'),
        localUrl: presentationUrl
    });

  } catch (error) {
    console.error("Error en generación:", error);
    return NextResponse.json({ error: error.message || "Error interno del servidor" }, { status: 500 });
  }
}
