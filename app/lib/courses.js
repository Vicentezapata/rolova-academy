import fs from 'fs/promises';
import path from 'path';
import { COURSES_ROOT } from './safePath';

const IGNORE_DIRS = new Set(['.vscode', '.git', 'node_modules', 'TRELLO', 'academy-portal']);
const MATERIAL_EXTENSIONS = new Set(['.html']);
const MAX_DEPTH = 5;

// Escanear cursos/ (cientos de MB) en cada request es caro; en dev se omite para ver los cambios al vuelo.
const CACHE_TTL_MS = process.env.NODE_ENV === 'production' ? 60_000 : 0;
const cache = new Map();

async function cached(key, produce) {
  if (CACHE_TTL_MS === 0) return produce();
  const hit = cache.get(key);
  if (hit && Date.now() - hit.at < CACHE_TTL_MS) return hit.value;
  const value = await produce();
  cache.set(key, { at: Date.now(), value });
  return value;
}

async function isFile(targetPath) {
  try {
    return (await fs.stat(targetPath)).isFile();
  } catch {
    return false;
  }
}

async function readCourseDirs() {
  const entries = await fs.readdir(COURSES_ROOT, { withFileTypes: true });
  return entries.filter((e) => e.isDirectory() && !IGNORE_DIRS.has(e.name) && !e.name.startsWith('.'));
}

async function scanFolder(currentPath, basePath, depth = 0) {
  if (depth > MAX_DEPTH) return [];

  const items = [];
  let entries;
  try {
    entries = await fs.readdir(currentPath, { withFileTypes: true });
  } catch (err) {
    console.error(`Error escaneando ${currentPath}:`, err);
    return items;
  }

  for (const entry of entries) {
    if (entry.name.startsWith('.')) continue;

    const fullPath = path.join(currentPath, entry.name);
    const relativePath = path.relative(basePath, fullPath);

    if (entry.isDirectory()) {
      // Una carpeta con preview.html es una presentación ya ensamblada: no se escanea dentro.
      if (await isFile(path.join(fullPath, 'preview.html'))) {
        items.push({
          type: 'ppt-output',
          name: entry.name,
          path: relativePath,
          previewUrl: path.join(relativePath, 'preview.html'),
        });
        continue;
      }

      const children = await scanFolder(fullPath, basePath, depth + 1);
      if (children.length > 0) {
        items.push({ type: 'folder', name: entry.name, path: relativePath, children });
      }
    } else if (entry.isFile()) {
      const ext = path.extname(entry.name).toLowerCase();
      if (MATERIAL_EXTENSIONS.has(ext)) {
        items.push({
          type: ext.slice(1),
          name: entry.name,
          path: relativePath,
          url: relativePath,
        });
      }
    }
  }

  return items;
}

/** Cursos con su árbol completo de materiales. */
export function listCoursesWithMaterials() {
  return cached('courses', async () => {
    const dirs = await readCourseDirs();
    return Promise.all(
      dirs.map(async (dir) => {
        const coursePath = path.join(COURSES_ROOT, dir.name);
        return {
          name: dir.name,
          path: dir.name,
          materials: await scanFolder(coursePath, coursePath),
        };
      })
    );
  });
}

/** Cursos con solo los nombres de sus unidades. */
export function listCourseUnits() {
  return cached('course-units', async () => {
    const dirs = await readCourseDirs();
    return Promise.all(
      dirs.map(async (dir) => {
        const entries = await fs.readdir(path.join(COURSES_ROOT, dir.name), { withFileTypes: true });
        const units = entries
          .filter((e) => e.isDirectory() && /UNIDAD|UNIT/i.test(e.name))
          .map((e) => e.name);
        return { name: dir.name, units };
      })
    );
  });
}
