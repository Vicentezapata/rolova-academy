"use client";

import { setPreference } from '../lib/theme-store';
import { useThemePreference } from '../lib/useTheme';

const OPTIONS = [
  { value: 'light',  icon: '☀️', label: 'Claro',   name: 'Tema claro' },
  { value: 'dark',   icon: '🌙', label: 'Oscuro',  name: 'Tema oscuro' },
  { value: 'system', icon: '💻', label: 'Sistema', name: 'Seguir el tema del sistema' },
];

export default function ThemeToggle() {
  const preference = useThemePreference();

  return (
    <div className="theme-toggle" role="radiogroup" aria-label="Tema de la interfaz">
      {OPTIONS.map((option) => (
        <button
          key={option.value}
          type="button"
          role="radio"
          aria-checked={preference === option.value}
          aria-label={option.name}
          className={`theme-toggle-option${preference === option.value ? ' is-active' : ''}`}
          onClick={() => setPreference(option.value)}
        >
          <span aria-hidden="true">{option.icon}</span>
          <span className="theme-toggle-label">{option.label}</span>
        </button>
      ))}
    </div>
  );
}
