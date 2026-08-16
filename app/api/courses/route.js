import { NextResponse } from 'next/server';
import { listCoursesWithMaterials } from '@/app/lib/courses';

export async function GET() {
  try {
    const courses = await listCoursesWithMaterials();
    return NextResponse.json({ courses });
  } catch (error) {
    console.error('Error reading directory:', error);
    return NextResponse.json({ error: 'Failed to read local filesystem' }, { status: 500 });
  }
}
