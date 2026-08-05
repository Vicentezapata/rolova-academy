"use client";

export default function HUD({ courses, loading, onCourseClick }) {
  return (
    <div className="hud-overlay">
      {/* Top bar */}
      <div className="hud-topbar">
        <div className="hud-brand">
          <div className="hud-brand-icon">🚀</div>
          <div>
            <div className="hud-title">Rolova Academy</div>
            <div className="hud-subtitle">Tu ecosistema de aprendizaje centralizado</div>
          </div>
        </div>
        <div className="hud-profile">
          <div className="hud-avatar">🧑‍🏫</div>
          <div className="hud-profile-info">
            <span className="hud-profile-name">Profesor</span>
            <span className="hud-profile-role">Administrador</span>
          </div>
        </div>
      </div>

      {/* Course sidebar legend */}
      <div className="hud-sidebar">
        <div className="hud-sidebar-title">📡 Estaciones Activas</div>
        {loading ? (
          <div className="hud-loader">Cargando...</div>
        ) : (
          courses.map((course, i) => {
            const colors = ['#d946ef', '#06b6d4', '#a855f7', '#f59e0b', '#10b981'];
            const icons = ['🎓', '🧠', '🔬', '🌐', '⚡'];
            return (
              <div key={i} className="hud-course-item" onClick={() => onCourseClick && onCourseClick(course)} style={{ cursor: 'pointer' }}>
                <div
                  className="hud-course-dot"
                  style={{ background: colors[i % colors.length] }}
                />
                <span className="hud-course-icon">{icons[i % icons.length]}</span>
                <span className="hud-course-name">{course.name}</span>
                <span className="hud-course-count">{course.materials.length}</span>
              </div>
            );
          })
        )}
      </div>


      {/* Controls hint */}
      <div className="hud-controls">
        <span>🖱️ Rotar</span>
        <span>⚙️ Scroll: Zoom</span>
        <span>🖱️ Clic: Abrir material</span>
      </div>
    </div>
  );
}
