"use client";

import { Suspense, useEffect, useState, useCallback } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, AdaptiveDpr, AdaptiveEvents, Preload } from '@react-three/drei';
import SpaceBackground from './components/SpaceBackground';
import SkillStation from './components/SkillStation';
import Rocket from './components/Rocket';
import HUD from './components/HUD';
import CoursePanel from './components/CoursePanel';
import './globals.css';

// Positions for up to 6 courses in a nice arc
const POSITIONS = [
  [-9,  0,  0],
  [-3,  1, -2],
  [ 3,  1, -2],
  [ 9,  0,  0],
  [-6, -2,  2],
  [ 6, -2,  2],
];

function stationPosition(index, total) {
  if (total <= 6) return POSITIONS[index] || [index * 8 - 4, 0, 0];
  const spread = total * 4;
  const angle  = (index / total) * Math.PI * 2;
  return [Math.cos(angle) * spread * 0.5, Math.sin(angle) * 2, 0];
}

function Scene({ courses, onSelect, selectedCourse }) {
  const selectedIndex = courses.findIndex(c => selectedCourse && c.name === selectedCourse.name);
  const targetPos = selectedIndex >= 0 ? stationPosition(selectedIndex, courses.length) : null;

  return (
    <>
      <SpaceBackground />
      {courses.map((course, i) => (
        <SkillStation
          key={i}
          course={course}
          position={stationPosition(i, courses.length)}
          courseIndex={i}
          onSelect={onSelect}
          isSelected={selectedCourse?.name === course.name}
        />
      ))}
      <Rocket targetPosition={targetPos} />
    </>
  );
}

export default function Home() {
  const [courses, setCourses]             = useState([]);
  const [loading, setLoading]             = useState(true);
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [selectedIndex, setSelectedIndex]   = useState(0);

  useEffect(() => {
    fetch('/api/courses')
      .then((r) => r.json())
      .then((d) => { setCourses(d.courses || []); setLoading(false); })
      .catch(() => setLoading(false));
  }, []);

  const handleSelect = useCallback((course) => {
    const idx = courses.findIndex((c) => c.name === course.name);
    setSelectedIndex(idx >= 0 ? idx : 0);
    setSelectedCourse((prev) => (prev?.name === course.name ? null : course));
  }, [courses]);

  const handleClose = useCallback(() => setSelectedCourse(null), []);

  return (
    <main style={{ width: '100vw', height: '100vh', overflow: 'hidden', background: '#050510' }}>
      {/* 3D Canvas */}
      <Canvas
        camera={{ position: [0, 3, 18], fov: 55 }}
        gl={{ antialias: true, alpha: false, powerPreference: 'high-performance' }}
        dpr={[1, 1.2]}
        frameloop="always"
        style={{ position: 'absolute', top: 0, left: 0 }}
      >
        <Suspense fallback={null}>
          {!loading && (
            <Scene
              courses={courses}
              onSelect={handleSelect}
              selectedCourse={selectedCourse}
            />
          )}
          <OrbitControls
            enablePan={false}
            enableZoom
            enableRotate
            maxDistance={30}
            minDistance={5}
            autoRotate={!selectedCourse && !loading}
            autoRotateSpeed={0.25}
            makeDefault
          />
          <AdaptiveDpr pixelated />
          <AdaptiveEvents />
          <Preload all />
        </Suspense>
      </Canvas>

      {/* HTML HUD overlay */}
      <HUD courses={courses} loading={loading} onCourseClick={handleSelect} />

      {/* Course detail panel */}
      {selectedCourse && (
        <CoursePanel
          course={selectedCourse}
          courseIndex={selectedIndex}
          onClose={handleClose}
        />
      )}

      {/* Loading splash */}
      {loading && (
        <div className="splash-loader">
          <div className="splash-ring" />
          <div className="splash-text">Inicializando Academia...</div>
        </div>
      )}
    </main>
  );
}
