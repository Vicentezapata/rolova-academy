"use client";

import { Suspense, useEffect, useState, useCallback } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, AdaptiveDpr, AdaptiveEvents, Preload } from '@react-three/drei';
import SpaceBackground from './components/SpaceBackground';
import SkillStation from './components/SkillStation';
import Rocket from './components/Rocket';
import HUD from './components/HUD';
import CoursePanel from './components/CoursePanel';
import { usePrefersReducedMotion, useResolvedTheme } from './lib/useTheme';
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

function Scene({ courses, onSelect, selectedCourse, theme, reducedMotion }) {
  const selectedIndex = courses.findIndex(c => selectedCourse && c.name === selectedCourse.name);
  const targetPos = selectedIndex >= 0 ? stationPosition(selectedIndex, courses.length) : null;

  return (
    <>
      <SpaceBackground theme={theme} />
      {courses.map((course, i) => (
        <SkillStation
          key={course.path || course.name}
          course={course}
          position={stationPosition(i, courses.length)}
          courseIndex={i}
          onSelect={onSelect}
          isSelected={selectedCourse?.name === course.name}
          reducedMotion={reducedMotion}
        />
      ))}
      <Rocket targetPosition={targetPos} reducedMotion={reducedMotion} />
    </>
  );
}

export default function Home() {
  const [courses, setCourses]             = useState([]);
  const [loading, setLoading]             = useState(true);
  const [error, setError]                 = useState(null);
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [selectedIndex, setSelectedIndex]   = useState(0);
  const [reloadToken, setReloadToken]     = useState(0);

  useEffect(() => {
    let cancelled = false;
    fetch('/api/courses')
      .then((r) => {
        if (!r.ok) throw new Error(`El servidor respondió ${r.status}`);
        return r.json();
      })
      .then((d) => {
        if (cancelled) return;
        setCourses(d.courses || []);
        setError(null);
      })
      .catch((err) => {
        if (!cancelled) setError(err.message || 'No se pudieron cargar los cursos.');
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => { cancelled = true; };
  }, [reloadToken]);

  const retry = useCallback(() => {
    setLoading(true);
    setError(null);
    setReloadToken((t) => t + 1);
  }, []);

  const handleSelect = useCallback((course) => {
    const idx = courses.findIndex((c) => c.name === course.name);
    setSelectedIndex(idx >= 0 ? idx : 0);
    setSelectedCourse((prev) => (prev?.name === course.name ? null : course));
  }, [courses]);

  const handleClose = useCallback(() => setSelectedCourse(null), []);

  const reducedMotion = usePrefersReducedMotion();
  const theme = useResolvedTheme();

  return (
    <main style={{ width: '100vw', height: '100vh', overflow: 'hidden', background: 'var(--bg-base)' }}>
      {/* 3D Canvas */}
      <Canvas
        camera={{ position: [0, 3, 18], fov: 55 }}
        gl={{ antialias: true, alpha: true, powerPreference: 'high-performance' }}
        dpr={[1, 1.2]}
        frameloop={reducedMotion ? 'demand' : 'always'}
        style={{ position: 'absolute', top: 0, left: 0 }}
      >
        <Suspense fallback={null}>
          {!loading && (
            <Scene
              courses={courses}
              onSelect={handleSelect}
              selectedCourse={selectedCourse}
              theme={theme}
              reducedMotion={reducedMotion}
            />
          )}
          <OrbitControls
            enablePan={false}
            enableZoom
            enableRotate
            maxDistance={30}
            minDistance={5}
            autoRotate={!selectedCourse && !loading && !reducedMotion}
            autoRotateSpeed={0.25}
            makeDefault
          />
          <AdaptiveDpr pixelated />
          <AdaptiveEvents />
          <Preload all />
        </Suspense>
      </Canvas>

      {/* HTML HUD overlay */}
      <HUD
        courses={courses}
        loading={loading}
        onCourseClick={handleSelect}
        selectedCourse={selectedCourse}
      />

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

      {/* Error state */}
      {!loading && error && (
        <div className="splash-loader" role="alert">
          <div className="splash-text">No se pudieron cargar los cursos.</div>
          <div className="splash-error-detail">{error}</div>
          <button className="splash-retry" onClick={retry}>Reintentar</button>
        </div>
      )}
    </main>
  );
}
