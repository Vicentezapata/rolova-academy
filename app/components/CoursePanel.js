"use client";
import { useCallback, useEffect, useId, useRef, useState } from 'react';
import { courseTheme } from '../lib/theme';

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

// Los nombres de curso/unidad llevan espacios y acentos: hay que codificar cada segmento.
function buildUrl(base, ...parts) {
  const segments = parts
    .join('/')
    .split(/[\\/]+/)
    .filter(Boolean)
    .map(encodeURIComponent);
  return `${base}/${segments.join('/')}`;
}

const buildFileUrl = (...parts) => buildUrl('/api/file', ...parts);
const buildDownloadUrl = (...parts) => buildUrl('/api/download', ...parts);

// Flatten a material tree into a grouped structure by folder (unit)
function groupMaterials(materials) {
  const units = [];
  const loose = [];

  for (const m of materials) {
    if (m.type === 'folder' && m.children && m.children.length > 0) {
      units.push({ name: m.name, path: m.path, items: m.children });
    } else {
      loose.push(m);
    }
  }

  if (loose.length > 0) {
    units.unshift({ name: 'Materiales Generales', path: null, items: loose });
  }

  return units;
}

function MaterialRow({ item, coursePath, accent }) {
  const icon  = TYPE_ICONS[item.type]  || TYPE_ICONS.default;
  const label = TYPE_LABELS[item.type] || TYPE_LABELS.default;

  const [isExporting, setIsExporting] = useState(false);
  const [exportError, setExportError] = useState(null);

  const url = item.type === 'ppt-output'
    ? buildFileUrl(coursePath, item.previewUrl)
    : buildFileUrl(coursePath, item.url);

  const handleOpen = () => {
    if (item.type === 'folder') return; // folder without preview, skip
    window.open(url, '_blank', 'noopener,noreferrer');
  };

  const handleExport = async () => {
    if (isExporting) return;
    
    setIsExporting(true);
    setExportError(null);
    try {
      const res = await fetch('/api/export-pptx', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          url: url,
          title: item.name.replace(/\.[^/.]+$/, '') 
        })
      });

      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        throw new Error(data.error || `El servidor respondió ${res.status}`);
      }

      const blob = await res.blob();
      const downloadUrl = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = downloadUrl;
      a.download = `${item.name.replace(/\.[^/.]+$/, '')}.pptx`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(downloadUrl);
    } catch (err) {
      setExportError(err.message || 'Hubo un error exportando la presentación.');
      console.error(err);
    } finally {
      setIsExporting(false);
    }
  };

  return (
    <div className="cp-material-row">
      <span className="cp-material-icon" aria-hidden="true">{icon}</span>
      <div className="cp-material-info">
        <span className="cp-material-name">{item.name.replace(/\.[^/.]+$/, '')}</span>
        <span className="cp-material-type">{label}</span>
        {exportError && <span className="cp-material-error" role="alert">{exportError}</span>}
      </div>
      
      {item.type === 'ppt-output' && (
        <button
          type="button"
          className="cp-open-btn cp-export-btn"
          style={{ '--accent': '#f59e0b' }}
          onClick={handleExport}
          disabled={isExporting}
        >
          {isExporting ? '⏳ Exportando...' : '📥 Exportar PPTX'}
        </button>
      )}

      {(item.type === 'folder' || item.type === 'ppt-output') && (
        <a
          className="cp-open-btn cp-download-btn"
          style={{ '--accent': accent }}
          href={buildDownloadUrl(coursePath, item.path)}
          download
        >
          <span aria-hidden="true">⬇</span> ZIP
          <span className="visually-hidden"> Descargar {item.name} comprimida</span>
        </a>
      )}

      {item.type !== 'folder' && (
        <button
          type="button"
          className="cp-open-btn is-primary"
          style={{ '--accent': accent }}
          onClick={handleOpen}
        >
          <span aria-hidden="true">▶</span> Abrir
          <span className="visually-hidden"> {item.name.replace(/\.[^/.]+$/, '')}</span>
        </button>
      )}
    </div>
  );
}

const FOCUSABLE = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';

export default function CoursePanel({ course, courseIndex, onClose }) {
  const panelRef = useRef(null);
  const titleId = useId();

  const handleKeyDown = useCallback((event) => {
    if (event.key === 'Escape') {
      event.stopPropagation();
      onClose();
      return;
    }
    if (event.key !== 'Tab') return;

    const focusables = panelRef.current?.querySelectorAll(FOCUSABLE);
    if (!focusables || focusables.length === 0) return;

    const first = focusables[0];
    const last = focusables[focusables.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }, [onClose]);

  useEffect(() => {
    const previouslyFocused = document.activeElement;
    panelRef.current?.querySelector(FOCUSABLE)?.focus();
    return () => {
      if (previouslyFocused instanceof HTMLElement) previouslyFocused.focus();
    };
  }, []);

  if (!course) return null;

  const theme = courseTheme(courseIndex);
  const groups = groupMaterials(course.materials);

  return (
    <div className="cp-overlay" onClick={onClose}>
      <div
        ref={panelRef}
        className="cp-panel"
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
        style={{ '--accent': theme.accent, '--glow': theme.glow, '--border': theme.border }}
        onClick={(e) => e.stopPropagation()}
        onKeyDown={handleKeyDown}
      >
        {/* Header */}
        <div className="cp-header">
          <div className="cp-header-icon" aria-hidden="true" style={{ background: `linear-gradient(135deg, ${theme.accent}, #1a0033)` }}>
            {theme.icon}
          </div>
          <div className="cp-header-text">
            <h2 id={titleId} className="cp-course-name">{course.name}</h2>
            <p className="cp-course-meta">{course.materials.length} materiales disponibles</p>
          </div>
          <button type="button" className="cp-close-btn" onClick={onClose} aria-label="Cerrar panel del curso">
            <span aria-hidden="true">✕</span>
          </button>
        </div>

        {/* Body: grouped by unit */}
        <div className="cp-body">
          {groups.length === 0 ? (
            <p className="cp-empty">No se encontraron materiales en este curso.</p>
          ) : (
            groups.map((group) => (
              <section key={group.name} className="cp-group">
                <h3 className="cp-group-title">
                  <span className="cp-group-bar" style={{ background: theme.accent }} aria-hidden="true" />
                  <span className="cp-group-name">{group.name}</span>
                  {group.path && (
                    <a
                      className="cp-unit-download"
                      href={buildDownloadUrl(course.path, group.path)}
                      download
                    >
                      <span aria-hidden="true">⬇</span> Descargar unidad
                      <span className="visually-hidden"> {group.name} comprimida</span>
                    </a>
                  )}
                </h3>
                <div className="cp-group-items">
                  {group.items.map((item) => (
                    <MaterialRow key={item.path} item={item} coursePath={course.path} accent={theme.accent} />
                  ))}
                </div>
              </section>
            ))
          )}
        </div>
      </div>
    </div>
  );
}
