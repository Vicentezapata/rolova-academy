import { NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';

// Directorios a ignorar en el nivel superior
const IGNORE_DIRS = ['.vscode', '.git', 'academy-portal', 'node_modules', 'TRELLO'];

async function isDirectory(targetPath) {
  try {
    const stat = await fs.stat(targetPath);
    return stat.isDirectory();
  } catch {
    return false;
  }
}

async function isFile(targetPath) {
  try {
    const stat = await fs.stat(targetPath);
    return stat.isFile();
  } catch {
    return false;
  }
}

// Función recursiva para buscar materiales
// Retorna un array de materiales o carpetas anidadas con materiales
async function scanFolder(currentPath, basePath) {
  const items = [];
  
  try {
    const entries = await fs.readdir(currentPath, { withFileTypes: true });
    
    for (const entry of entries) {
      const fullPath = path.join(currentPath, entry.name);
      // Ruta relativa desde la raíz del curso
      const relativePath = path.relative(basePath, fullPath);
      
      // Ignorar archivos ocultos o de sistema
      if (entry.name.startsWith('.')) continue;

      if (entry.isDirectory()) {
        // ¿Es una carpeta ppt-output?
        // Comprobamos si tiene un preview.html
        const previewPath = path.join(fullPath, 'preview.html');
        if (await isFile(previewPath)) {
          items.push({
            type: 'ppt-output',
            name: entry.name,
            path: relativePath,
            previewUrl: relativePath + '/preview.html'
          });
          continue; // No escanear dentro de ppt-output
        }
        
        // Si no es un material directo, escaneamos sus hijos
        const children = await scanFolder(fullPath, basePath);
        if (children.length > 0) {
          items.push({
            type: 'folder',
            name: entry.name,
            path: relativePath,
            children
          });
        }
      } else if (entry.isFile()) {
        const ext = path.extname(entry.name).toLowerCase();
        // Incluir solo HTML
        if (['.html'].includes(ext)) {
          items.push({
            type: ext.substring(1), // html
            name: entry.name,
            path: relativePath,
            url: relativePath
          });
        }
      }
    }
  } catch (err) {
    console.error(`Error escaneando ${currentPath}:`, err);
  }
  
  return items;
}

export async function GET() {
  try {
    // La raíz de los cursos es el directorio padre de `academy-portal`
    const rootPath = path.join(process.cwd(), '..');
    
    const entries = await fs.readdir(rootPath, { withFileTypes: true });
    
    const courses = [];

    for (const entry of entries) {
      if (entry.isDirectory() && !IGNORE_DIRS.includes(entry.name)) {
        const coursePath = path.join(rootPath, entry.name);
        
        // Escanear el curso
        const materials = await scanFolder(coursePath, coursePath);
        
        // Solo agregar el curso si tiene algún material (o siempre agregarlo)
        courses.push({
          name: entry.name,
          path: entry.name,
          materials
        });
      }
    }

    return NextResponse.json({ courses });
  } catch (error) {
    console.error("Error reading directory:", error);
    return NextResponse.json({ error: 'Failed to read local filesystem' }, { status: 500 });
  }
}
