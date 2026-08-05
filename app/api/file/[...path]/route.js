import { NextResponse } from 'next/server';
import fs from 'fs/promises';
import { createReadStream } from 'fs';
import path from 'path';

const mimeTypes = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.pdf': 'application/pdf',
  '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
  '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  '.txt': 'text/plain'
};

export async function GET(request, { params }) {
  try {
    const resolvedParams = await params;
    const filePathArray = resolvedParams.path;
    const rootPath = path.join(process.cwd(), '..');
    
    // Unir la ruta y prevenir salir del directorio raíz padre
    const requestedPath = path.join(rootPath, ...filePathArray);
    
    // Verificación básica de seguridad para evitar Directory Traversal
    if (!requestedPath.startsWith(rootPath)) {
        return new NextResponse('Forbidden', { status: 403 });
    }

    try {
      const stat = await fs.stat(requestedPath);
      if (!stat.isFile()) {
        return new NextResponse('Not found', { status: 404 });
      }
    } catch {
      return new NextResponse('Not found', { status: 404 });
    }

    const ext = path.extname(requestedPath).toLowerCase();
    const contentType = mimeTypes[ext] || 'application/octet-stream';

    // Leer el archivo
    const fileBuffer = await fs.readFile(requestedPath);

    return new NextResponse(fileBuffer, {
      status: 200,
      headers: {
        'Content-Type': contentType,
        // Evitar el almacenamiento en caché agresivo en desarrollo
        'Cache-Control': 'no-store, max-age=0'
      }
    });
  } catch (error) {
    console.error("Error serving file:", error);
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}
