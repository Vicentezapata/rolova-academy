"use client";

const TYPE_ICONS = {
  html: '🖥️',
  'ppt-output': '📊',
  folder: '📁',
  default: '📎',
};

const TYPE_LABELS = {
  html: 'Presentación HTML',
  'ppt-output': 'Presentación PPT',
  folder: 'Carpeta de unidad',
  default: 'Archivo',
};

const COURSE_THEMES = [
  { accent: '#d946ef', glow: 'rgba(217,70,239,0.25)', border: 'rgba(217,70,239,0.35)' },
  { accent: '#06b6d4', glow: 'rgba(6,182,212,0.25)',  border: 'rgba(6,182,212,0.35)'  },
  { accent: '#a855f7', glow: 'rgba(168,85,247,0.25)', border: 'rgba(168,85,247,0.35)' },
  { accent: '#f59e0b', glow: 'rgba(245,158,11,0.25)', border: 'rgba(245,158,11,0.35)' },
  { accent: '#10b981', glow: 'rgba(16,185,129,0.25)', border: 'rgba(16,185,129,0.35)' },
];

const COURSE_ICONS = ['🎓', '🧠', '🔬', '🌐', '⚡'];

// Flatten a material tree into a grouped structure by folder (unit)
function groupMaterials(materials) {
  const units = [];
  const loose = [];

  for (const m of materials) {
    if (m.type === 'folder' && m.children && m.children.length > 0) {
      units.push({ name: m.name, items: m.children });
    } else {
      loose.push(m);
    }
  }

  if (loose.length > 0) {
    units.unshift({ name: 'Materiales Generales', items: loose });
  }

  return units;
}

function MaterialRow({ item, coursePath, accent }) {
  const icon  = TYPE_ICONS[item.type]  || TYPE_ICONS.default;
  const label = TYPE_LABELS[item.type] || TYPE_LABELS.default;

  const url = item.type === 'ppt-output'
    ? `/api/file/${coursePath}/${item.previewUrl}`
    : `/api/file/${coursePath}/${item.url}`;

  const handleOpen = () => {
    if (item.type === 'folder') return; // folder without preview, skip
    window.open(url, '_blank');
  };

  return (
    <div className="cp-material-row" onClick={handleOpen} style={{ cursor: item.type === 'folder' ? 'default' : 'pointer' }}>
      <span className="cp-material-icon">{icon}</span>
      <div className="cp-material-info">
        <span className="cp-material-name">{item.name.replace(/\.[^/.]+$/, '')}</span>
        <span className="cp-material-type">{label}</span>
      </div>
      {item.type !== 'folder' && (
        <button className="cp-open-btn" style={{ '--accent': accent }} onClick={(e) => { e.stopPropagation(); handleOpen(); }}>
          ▶ Abrir
        </button>
      )}
    </div>
  );
}

export default function CoursePanel({ course, courseIndex, onClose }) {
  if (!course) return null;

  const theme = COURSE_THEMES[courseIndex % COURSE_THEMES.length];
  const icon  = COURSE_ICONS[courseIndex % COURSE_ICONS.length];
  const groups = groupMaterials(course.materials);

  return (
    <div className="cp-overlay" onClick={onClose}>
      <div
        className="cp-panel"
        style={{ '--accent': theme.accent, '--glow': theme.glow, '--border': theme.border }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="cp-header">
          <div className="cp-header-icon" style={{ background: `linear-gradient(135deg, ${theme.accent}, #1a0033)` }}>
            {icon}
          </div>
          <div className="cp-header-text">
            <div className="cp-course-name">{course.name}</div>
            <div className="cp-course-meta">{course.materials.length} materiales disponibles</div>
          </div>
          <button className="cp-close-btn" onClick={onClose}>✕</button>
        </div>

        {/* Body: grouped by unit */}
        <div className="cp-body">
          {groups.length === 0 ? (
            <p className="cp-empty">No se encontraron materiales en este curso.</p>
          ) : (
            groups.map((group, gi) => (
              <div key={gi} className="cp-group">
                <div className="cp-group-title">
                  <span className="cp-group-bar" style={{ background: theme.accent }} />
                  {group.name}
                </div>
                <div className="cp-group-items">
                  {group.items.map((item, ii) => (
                    <MaterialRow key={ii} item={item} coursePath={course.path} accent={theme.accent} />
                  ))}
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}
