"use client";

const STORAGE_KEY = 'rolova-theme';
const listeners = new Set();

let preference = 'system';
let resolved = 'dark';
let initialised = false;

function systemIsDark() {
  return window.matchMedia('(prefers-color-scheme: dark)').matches;
}

function resolve(pref) {
  return pref === 'system' ? (systemIsDark() ? 'dark' : 'light') : pref;
}

function ensureInit() {
  if (initialised) return;
  initialised = true;
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    preference = stored === 'light' || stored === 'dark' ? stored : 'system';
  } catch {
    preference = 'system';
  }
  resolved = resolve(preference);
}

function notify() {
  listeners.forEach((listener) => listener());
}

export function subscribe(listener) {
  ensureInit();
  listeners.add(listener);
  const mq = window.matchMedia('(prefers-color-scheme: dark)');
  const onSystemChange = () => {
    if (preference !== 'system') return;
    resolved = resolve(preference);
    notify();
  };
  mq.addEventListener('change', onSystemChange);
  return () => {
    listeners.delete(listener);
    mq.removeEventListener('change', onSystemChange);
  };
}

export function getPreference() {
  if (typeof window === 'undefined') return 'system';
  ensureInit();
  return preference;
}

export function getResolvedTheme() {
  if (typeof window === 'undefined') return 'dark';
  ensureInit();
  return resolved;
}

export const getServerPreference = () => 'system';
export const getServerTheme = () => 'dark';

export function setPreference(next) {
  ensureInit();
  preference = next;
  resolved = resolve(next);

  const root = document.documentElement;
  if (next === 'system') root.removeAttribute('data-theme');
  else root.setAttribute('data-theme', next);
  root.style.colorScheme = resolved;

  try {
    if (next === 'system') localStorage.removeItem(STORAGE_KEY);
    else localStorage.setItem(STORAGE_KEY, next);
  } catch {
    // almacenamiento no disponible: el tema dura solo esta sesión
  }

  notify();
}

/** Se ejecuta antes del primer pintado para evitar el parpadeo de tema. */
export const NO_FLASH_SCRIPT = `(function(){try{var p=localStorage.getItem('${STORAGE_KEY}');if(p==='light'||p==='dark'){document.documentElement.setAttribute('data-theme',p);document.documentElement.style.colorScheme=p;}}catch(e){}})();`;
