import { NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';
import { COURSES_ROOT, realPathInsideRoot } from '@/app/lib/safePath';

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
    const { path: filePathArray } = await params;
    if (!Array.isArray(filePathArray) || filePathArray.length === 0) {
      return new NextResponse('Not found', { status: 404 });
    }

    // Resuelve symlinks y rechaza cualquier ruta que escape de cursos/
    const requestedPath = await realPathInsideRoot(COURSES_ROOT, ...filePathArray);
    if (!requestedPath) {
      return new NextResponse('Forbidden', { status: 403 });
    }

    const stat = await fs.stat(requestedPath);
    if (!stat.isFile()) {
      return new NextResponse('Not found', { status: 404 });
    }

    const ext = path.extname(requestedPath).toLowerCase();
    const contentType = mimeTypes[ext] || 'application/octet-stream';
    const fileBuffer = await fs.readFile(requestedPath);

    return new NextResponse(fileBuffer, {
      status: 200,
      headers: {
        'Content-Type': contentType,
        'X-Content-Type-Options': 'nosniff',
        'Cache-Control': 'no-store, max-age=0'
      }
    });
  } catch (error) {
    if (error?.code === 'ENOENT') {
      return new NextResponse('Not found', { status: 404 });
    }
    console.error('Error serving file:', error);
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}
