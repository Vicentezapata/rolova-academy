import { NextResponse } from 'next/server';

import { GET as getCourses } from '@/app/lib/handlers/courses';
import { GET as getCourseUnits } from '@/app/lib/handlers/courseUnits';
import { GET as getDownload } from '@/app/lib/handlers/download';
import { GET as getFile } from '@/app/lib/handlers/file';
import { POST as postExportPptx } from '@/app/lib/handlers/exportPptx';
import { POST as postGeneratePresentation } from '@/app/lib/handlers/generatePresentation';

export async function GET(request, { params }) {
  const resolvedParams = await params;
  const catchall = resolvedParams.catchall;
  
  if (!catchall || catchall.length === 0) {
    return new NextResponse('Not found', { status: 404 });
  }

  const routeName = catchall[0];

  if (routeName === 'courses') {
    return getCourses(request, { params: Promise.resolve({}) });
  }
  
  if (routeName === 'course-units') {
    return getCourseUnits(request, { params: Promise.resolve({}) });
  }
  
  if (routeName === 'download') {
    const pathSegments = catchall.slice(1);
    return getDownload(request, { params: Promise.resolve({ path: pathSegments }) });
  }
  
  if (routeName === 'file') {
    const pathSegments = catchall.slice(1);
    return getFile(request, { params: Promise.resolve({ path: pathSegments }) });
  }
  
  return new NextResponse('Not found', { status: 404 });
}

export async function POST(request, { params }) {
  const resolvedParams = await params;
  const catchall = resolvedParams.catchall;
  
  if (!catchall || catchall.length === 0) {
    return new NextResponse('Not found', { status: 404 });
  }

  const routeName = catchall[0];

  if (routeName === 'export-pptx') {
    return postExportPptx(request, { params: Promise.resolve({}) });
  }
  
  if (routeName === 'generate-presentation') {
    return postGeneratePresentation(request, { params: Promise.resolve({}) });
  }

  return new NextResponse('Not found', { status: 404 });
}
