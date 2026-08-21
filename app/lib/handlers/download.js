import { NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';
import { Readable } from 'stream';
import { ZipArchive } from 'archiver';
import { COURSES_ROOT, realPathInsideRoot } from '@/app/lib/safePath';

function contentDisposition(folderName) {
  // Los nombres llevan tildes y espacios: filename ASCII de respaldo + filename* en UTF-8.
  const ascii = folderName.replace(/[^\w.-]+/g, '_').replace(/^_+|_+$/g, '') || 'material';
  return `attachment; filename="${ascii}.zip"; filename*=UTF-8''${encodeURIComponent(folderName)}.zip`;
}

export async function GET(request, { params }) {
  try {
    const { path: segments } = await params;
    if (!Array.isArray(segments) || segments.length === 0) {
      return new NextResponse('Not found', { status: 404 });
    }

    const dir = await realPathInsideRoot(COURSES_ROOT, ...segments);
    if (!dir) {
      return new NextResponse('Forbidden', { status: 403 });
    }

    const stat = await fs.stat(dir);
    if (!stat.isDirectory()) {
      return new NextResponse('Solo se pueden descargar carpetas', { status: 400 });
    }

    const archive = new ZipArchive({ zlib: { level: 6 } });
    archive.on('error', (err) => {
      console.error('[Download] Error comprimiendo:', err);
      archive.destroy(err);
    });
    // No seguir symlinks: evita sacar por el ZIP archivos de fuera de cursos/
    archive.directory(dir, path.basename(dir), { follow: false });
    archive.finalize();

    return new NextResponse(Readable.toWeb(archive), {
      status: 200,
      headers: {
        'Content-Type': 'application/zip',
        'Content-Disposition': contentDisposition(path.basename(dir)),
        'X-Content-Type-Options': 'nosniff',
        'Cache-Control': 'no-store',
      },
    });
  } catch (error) {
    if (error?.code === 'ENOENT') {
      return new NextResponse('Not found', { status: 404 });
    }
    console.error('[Download] Error:', error);
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}
