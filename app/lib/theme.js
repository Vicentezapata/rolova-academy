// Fuente unica de la paleta por curso: la usan HUD, CoursePanel y SkillStation.
export const COURSE_THEMES = [
  { accent: '#d946ef', ring: '#f0abfc', core: 'plasma',   icon: '🎓' },
  { accent: '#06b6d4', ring: '#67e8f9', core: 'crystal',  icon: '🧠' },
  { accent: '#a855f7', ring: '#d8b4fe', core: 'hologram', icon: '🔬' },
  { accent: '#f59e0b', ring: '#fde68a', core: 'energy',   icon: '🌐' },
  { accent: '#10b981', ring: '#6ee7b7', core: 'glass',    icon: '⚡' },
];

function withAlpha(hex, alpha) {
  const r = parseInt(hex.slice(1, 3), 16);
  const g = parseInt(hex.slice(3, 5), 16);
  const b = parseInt(hex.slice(5, 7), 16);
  return `rgba(${r},${g},${b},${alpha})`;
}

export function courseTheme(index) {
  const base = COURSE_THEMES[index % COURSE_THEMES.length];
  return {
    ...base,
    glow: withAlpha(base.accent, 0.25),
    border: withAlpha(base.accent, 0.35),
  };
}
