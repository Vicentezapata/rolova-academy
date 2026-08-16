"use client";

import { useSyncExternalStore } from 'react';
import {
  subscribe,
  getPreference,
  getResolvedTheme,
  getServerPreference,
  getServerTheme,
} from './theme-store';

/** Preferencia elegida por el usuario: 'light' | 'dark' | 'system'. */
export function useThemePreference() {
  return useSyncExternalStore(subscribe, getPreference, getServerPreference);
}

/** Tema realmente aplicado: 'light' | 'dark'. */
export function useResolvedTheme() {
  return useSyncExternalStore(subscribe, getResolvedTheme, getServerTheme);
}

const REDUCED_MOTION_QUERY = '(prefers-reduced-motion: reduce)';

function subscribeReducedMotion(listener) {
  const mq = window.matchMedia(REDUCED_MOTION_QUERY);
  mq.addEventListener('change', listener);
  return () => mq.removeEventListener('change', listener);
}

export function usePrefersReducedMotion() {
  return useSyncExternalStore(
    subscribeReducedMotion,
    () => window.matchMedia(REDUCED_MOTION_QUERY).matches,
    () => false
  );
}
