"use client";

import { useRef, useMemo } from 'react';
import { useFrame } from '@react-three/fiber';
import { Stars } from '@react-three/drei';
import * as THREE from 'three';

// PRNG determinista: Math.random() en render regeneraria la nebulosa en cada re-render.
function mulberry32(seed) {
  return function () {
    seed |= 0;
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function NebulaCloud({ color, count = 400, spread = 28, offsetX = 0, offsetY = 0, offsetZ = -22, opacity = 0.45 }) {
  const ref = useRef();
  const positions = useMemo(() => {
    const random = mulberry32(count * 73856093 + spread * 19349663 + offsetX * 83492791);
    const arr = new Float32Array(count * 3);
    for (let i = 0; i < count; i++) {
      arr[i * 3]     = (random() - 0.5) * spread + offsetX;
      arr[i * 3 + 1] = (random() - 0.5) * (spread * 0.4) + offsetY;
      arr[i * 3 + 2] = (random() - 0.5) * spread + offsetZ;
    }
    return arr;
  }, [count, spread, offsetX, offsetY, offsetZ]);

  useFrame((state) => {
    if (ref.current) {
      ref.current.rotation.y = state.clock.elapsedTime * 0.008;
    }
  });

  return (
    <points ref={ref}>
      <bufferGeometry>
        <bufferAttribute attach="attributes-position" array={positions} count={count} itemSize={3} />
      </bufferGeometry>
      <pointsMaterial color={color} size={0.1} transparent opacity={opacity} sizeAttenuation depthWrite={false} />
    </points>
  );
}

export default function SpaceBackground({ theme = 'dark' }) {
  const isLight = theme === 'light';

  return (
    <>
      <Stars
        radius={100}
        depth={50}
        count={isLight ? 900 : 3000}
        factor={4}
        saturation={0.3}
        fade
        speed={0.4}
      />
      <NebulaCloud color="#d946ef" count={400} spread={30} offsetX={-15} offsetY={4} offsetZ={-22} opacity={isLight ? 0.22 : 0.45} />
      <NebulaCloud color="#06b6d4" count={400} spread={30} offsetX={15}  offsetY={-4} offsetZ={-22} opacity={isLight ? 0.22 : 0.45} />
      <NebulaCloud color="#8b5cf6" count={250} spread={22} offsetX={0}   offsetY={8}  offsetZ={-28} opacity={isLight ? 0.22 : 0.45} />
      <ambientLight intensity={isLight ? 1.1 : 0.3} color={isLight ? '#ffffff' : '#1a0033'} />
      <pointLight position={[-10, 4, 2]} intensity={25} color="#d946ef" distance={22} />
      <pointLight position={[10, -4, 2]} intensity={25} color="#06b6d4" distance={22} />
    </>
  );
}
