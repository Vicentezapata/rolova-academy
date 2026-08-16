"use client";

import React, { useState } from 'react';
import { Wand2, Loader2, CheckCircle2, ExternalLink } from 'lucide-react';
import styles from './page.module.css';

export default function GeneradorPresentaciones() {
  const [topic, setTopic] = useState('La Unidad 4');
  const [selectedCourse, setSelectedCourse] = useState('');
  const [selectedUnit, setSelectedUnit] = useState('');
  const [coursesData, setCoursesData] = useState([]);
  
  const [mode, setMode] = useState('standard');
  const [theme, setTheme] = useState('dark_tech');
  const [investigate, setInvestigate] = useState(true);
  
  const [isGenerating, setIsGenerating] = useState(false);
  const [status, setStatus] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  React.useEffect(() => {
    fetch('/api/course-units')
      .then(res => res.json())
      .then(data => {
        if (data.courses) {
          setCoursesData(data.courses);
          if (data.courses.length > 0) {
            setSelectedCourse(data.courses[0].name);
          }
        }
      })
      .catch(err => console.error("Error fetching courses", err));
  }, []);

  const handleGenerate = async () => {
    setIsGenerating(true);
    setError(null);
    setResult(null);
    setStatus('Iniciando proceso mágico...');

    try {
      setStatus('Ingestando documentos y analizando con IA...');
      const response = await fetch('/api/generate-presentation', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic, selectedCourse, selectedUnit, theme, mode, investigate }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Error desconocido del servidor');
      }

      setStatus('¡Ensamblaje completado!');
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1>Generador de Presentaciones IA (Zero-Click)</h1>
        <p className={styles.desc}>
          Configura los parámetros y deja que el orquestador ingeste tu material, diseñe la clase con Gemini y ensamble el HTML automáticamente.
        </p>
      </div>

      <div className={styles.gridLayout}>
        {/* Controles */}
        <div className={styles.panel}>
          <h2>1. Configuración de la Clase</h2>
          
          <div className={styles.formGroup}>
            <label htmlFor="topic">Tema o Título</label>
            <input 
              type="text" 
              id="topic" 
              className={styles.input}
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              placeholder="Ej: Unidad 4 de Desarrollo Web" 
            />
          </div>
          
          <div className={styles.formGroup}>
            <label htmlFor="course">Curso</label>
            <select 
              id="course" 
              className={styles.input}
              value={selectedCourse}
              onChange={(e) => {
                setSelectedCourse(e.target.value);
                setSelectedUnit('');
              }}
            >
              {coursesData.map(c => (
                <option key={c.name} value={c.name}>{c.name}</option>
              ))}
            </select>
          </div>

          <div className={styles.formGroup}>
            <label htmlFor="unit">Unidad (carpeta que contiene el material)</label>
            <select 
              id="unit" 
              className={styles.input}
              value={selectedUnit}
              onChange={(e) => setSelectedUnit(e.target.value)}
            >
              <option value="">-- Seleccionar Unidad --</option>
              {coursesData.find(c => c.name === selectedCourse)?.units?.map(unitName => (
                  <option key={unitName} value={unitName}>{unitName}</option>
              ))}
            </select>
          </div>
          
          <div className={styles.formGroup}>
            <label htmlFor="mode">Modo de Ensamblaje</label>
            <select 
              id="mode" 
              className={styles.input}
              value={mode}
              onChange={(e) => setMode(e.target.value)}
            >
              <option value="standard">Modo Estándar (Componentes + Style Gallery)</option>
              {/* Añadiremos Full-Deck luego si es necesario */}
            </select>
          </div>
          
          <div className={styles.formGroup}>
            <label htmlFor="theme">Selecciona el Template / Estilo</label>
            <select 
              id="theme" 
              className={styles.input}
              value={theme}
              onChange={(e) => setTheme(e.target.value)}
            >
              <option value="dark_tech">Dark Tech</option>
              <option value="liquid_glass">Liquid Glass</option>
              <option value="cyberpunk_neon">Cyberpunk Neon</option>
              <option value="retro_70s">Retro 70s</option>
              <option value="minimal_gray">Minimal Gray</option>
              <option value="blue_white">Blue White</option>
              <option value="noir_film">Noir Film</option>
              <option value="bauhaus_block">Bauhaus Block</option>
              <option value="botanic_forest">Botanic Forest</option>
              <option value="candy_pastel">Candy Pastel</option>
            </select>
          </div>
          
          <div className={styles.checkboxGroup}>
            <input 
              type="checkbox" 
              id="investigate" 
              checked={investigate}
              onChange={(e) => setInvestigate(e.target.checked)}
            />
            <label htmlFor="investigate">Permitir a la IA investigar y expandir contenido</label>
          </div>
        </div>

        {/* Generación y Resultados */}
        <div className={styles.panel}>
          <h2>2. Magia Agentic</h2>
          
          <div className={styles.previewContainer}>
             <p style={{ color: 'var(--text-secondary)' }}>Tema Seleccionado: {theme}</p>
          </div>
          
          <button 
            className={styles.button}
            onClick={handleGenerate}
            disabled={isGenerating || !selectedCourse || !selectedUnit}
          >
            {isGenerating ? (
              <><Loader2 className="animate-spin" /> Generando...</>
            ) : (
              <><Wand2 /> Generar Presentación Mágicamente</>
            )}
          </button>

          {!selectedUnit && (
            <p style={{ fontSize: '0.8rem', marginTop: '0.5rem', color: 'var(--text-secondary)' }}>
              Selecciona una unidad para habilitar la generación.
            </p>
          )}

          {isGenerating && (
            <div className={styles.statusBox} role="status" aria-live="polite">
              <div className={styles.statusTitle}>Estado del Agente</div>
              <div className={styles.statusText}>{status}</div>
            </div>
          )}

          {error && (
            <div className={styles.statusBox} role="alert" style={{borderColor: 'var(--danger)', backgroundColor: 'rgba(239, 68, 68, 0.1)'}}>
              <div className={styles.statusTitle} style={{color: 'var(--danger)'}}>Error</div>
              <div className={styles.statusText} style={{color: 'var(--danger)'}}>{error}</div>
            </div>
          )}

          {result && (
            <div className={styles.successBox}>
              <div className={styles.successTitle} style={{display: 'flex', alignItems: 'center', gap: '0.5rem'}}>
                <CheckCircle2 size={20} />
                ¡Presentación Creada!
              </div>
              <div style={{marginTop: '1rem'}}>
                <p>Ubicación: <code>{result.presentationPath}</code></p>
                <a 
                   href={result.previewUrl} 
                   target="_blank" 
                   rel="noopener noreferrer"
                   style={{
                     display: 'inline-flex', 
                     alignItems: 'center', 
                     gap: '0.5rem',
                     marginTop: '1rem',
                     padding: '0.5rem 1rem',
                     backgroundColor: '#10b981',
                     color: '#fff',
                     textDecoration: 'none',
                     borderRadius: '4px',
                     fontWeight: 'bold'
                   }}
                >
                  <ExternalLink size={16} /> Abrir presentación
                </a>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
