import { NextResponse } from 'next/server';
import { listCourseUnits } from '@/app/lib/courses';

export async function GET() {
  try {
    const courses = await listCourseUnits();
    return NextResponse.json({ courses });
  } catch (error) {
    if (error?.code === 'ENOENT') {
      return NextResponse.json({ courses: [] });
    }
    console.error('Error leyendo directorios de cursos:', error);
    return NextResponse.json({ error: 'Fallo al leer el sistema de archivos' }, { status: 500 });
  }
}
