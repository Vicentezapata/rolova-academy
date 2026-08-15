import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

const IGNORE_DIRS = ['.vscode', '.git', 'node_modules', 'TRELLO'];

export async function GET() {
  try {
    const rootPath = path.join(process.cwd(), 'cursos');
    if (!fs.existsSync(rootPath)) {
        return NextResponse.json({ courses: [] });
    }

    const entries = fs.readdirSync(rootPath, { withFileTypes: true });
    const courses = [];

    for (const entry of entries) {
      if (entry.isDirectory() && !IGNORE_DIRS.includes(entry.name)) {
        const coursePath = path.join(rootPath, entry.name);
        const subEntries = fs.readdirSync(coursePath, { withFileTypes: true });
        
        const units = subEntries
          .filter(e => e.isDirectory() && (e.name.toUpperCase().includes('UNIDAD') || e.name.toUpperCase().includes('UNIT')))
          .map(e => e.name);
          
        courses.push({
          name: entry.name,
          units: units
        });
      }
    }

    return NextResponse.json({ courses });
  } catch (error) {
    console.error("Error leyendo directorios de cursos:", error);
    return NextResponse.json({ error: 'Fallo al leer el sistema de archivos' }, { status: 500 });
  }
}
