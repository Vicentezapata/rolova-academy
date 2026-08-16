import fs from 'fs/promises';
import path from 'path';

export const COURSES_ROOT = path.join(process.cwd(), 'cursos');

function isInside(root, target) {
  return target === root || target.startsWith(root + path.sep);
}

/** Resuelve segmentos contra `root` y devuelve null si el resultado se sale de él. */
export function resolveInsideRoot(root, ...segments) {
  if (segments.some((s) => typeof s !== 'string' || s.length === 0)) return null;
  const resolved = path.resolve(root, ...segments);
  return isInside(root, resolved) ? resolved : null;
}

/** Igual que resolveInsideRoot pero además resuelve symlinks para evitar escapes indirectos. */
export async function realPathInsideRoot(root, ...segments) {
  const resolved = resolveInsideRoot(root, ...segments);
  if (!resolved) return null;
  try {
    const [realTarget, realRoot] = await Promise.all([
      fs.realpath(resolved),
      fs.realpath(root),
    ]);
    return isInside(realRoot, realTarget) ? realTarget : null;
  } catch {
    return null;
  }
}

/** Construye la URL pública servida por /api/file a partir de una ruta absoluta dentro de cursos/. */
export function toFileApiUrl(absolutePath) {
  const relative = path.relative(COURSES_ROOT, absolutePath);
  if (!relative || relative.startsWith('..')) return null;
  const segments = relative.split(path.sep).map(encodeURIComponent);
  return `/api/file/${segments.join('/')}`;
}
