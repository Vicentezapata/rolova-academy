"use client";

import Link from 'next/link';
import { courseTheme } from '../lib/theme';
import ThemeToggle from './ThemeToggle';

export default function HUD({ courses, loading, onCourseClick, selectedCourse }) {
  return (
    <div className="hud-overlay">
      {/* Top bar */}
      <header className="hud-topbar">
        <div className="hud-brand">
          <div className="hud-brand-icon" aria-hidden="true">🚀</div>
          <div>
            <div className="hud-title">Rolova Academy</div>
            <div className="hud-subtitle">Tu ecosistema de aprendizaje centralizado</div>
          </div>
        </div>
        <div className="hud-actions">
          <ThemeToggle />
          <Link href="/presentaciones/nuevo" className="hud-cta" aria-label="Crear una nueva presentación">
            <span aria-hidden="true">✨</span>
            <span className="hud-cta-label">Nueva presentación</span>
          </Link>
          <div className="hud-profile">
            <div className="hud-avatar" aria-hidden="true">🧑‍🏫</div>
            <div className="hud-profile-info">
              <span className="hud-profile-name">Profesor</span>
              <span className="hud-profile-role">Administrador</span>
            </div>
          </div>
        </div>
      </header>

      {/* Course sidebar legend */}
      <nav className="hud-sidebar" aria-label="Cursos disponibles">
        <h2 className="hud-sidebar-title">
          <span aria-hidden="true">📡</span> Estaciones Activas
        </h2>
        {loading ? (
          <p className="hud-loader">Cargando...</p>
        ) : (
          courses.map((course, i) => {
            const theme = courseTheme(i);
            const isSelected = selectedCourse?.name === course.name;
            return (
              <button
                key={course.path || course.name}
                type="button"
                className="hud-course-item"
                aria-pressed={isSelected}
                onClick={() => onCourseClick && onCourseClick(course)}
              >
                <span className="hud-course-dot" style={{ background: theme.accent }} aria-hidden="true" />
                <span className="hud-course-icon" aria-hidden="true">{theme.icon}</span>
                <span className="hud-course-name">{course.name}</span>
                <span className="hud-course-count">
                  {course.materials.length}
                  <span className="visually-hidden"> materiales</span>
                </span>
              </button>
            );
          })
        )}
      </nav>


      {/* Controls hint */}
      <div className="hud-controls" aria-hidden="true">
        <span>🖱️ Rotar</span>
        <span>⚙️ Scroll: Zoom</span>
        <span>🖱️ Clic: Abrir material</span>
      </div>
    </div>
  );
}
