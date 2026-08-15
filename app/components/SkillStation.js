"use client";

import { useRef } from 'react';
import { useFrame } from '@react-three/fiber';
import { Html, MeshDistortMaterial, MeshWobbleMaterial } from '@react-three/drei';

const COURSE_THEMES = [
  { color: '#d946ef', ring: '#f0abfc', type: 'plasma' },
  { color: '#06b6d4', ring: '#67e8f9', type: 'crystal' },
  { color: '#a855f7', ring: '#d8b4fe', type: 'hologram' },
  { color: '#f59e0b', ring: '#fde68a', type: 'energy' },
  { color: '#10b981', ring: '#6ee7b7', type: 'glass' },
];

const COURSE_ICONS = ['🎓', '🧠', '🔬', '🌐', '⚡'];

function PlanetCore({ theme, isSelected }) {
  const emissiveIntensity = isSelected ? 2.5 : 1.0;
  
  switch(theme.type) {
    case 'plasma':
      return (
        <mesh>
          <sphereGeometry args={[0.85, 64, 64]} />
          <MeshDistortMaterial 
            color={theme.color} emissive={theme.color} emissiveIntensity={emissiveIntensity} 
            distort={0.5} speed={4} roughness={0.2} metalness={0.8}
          />
        </mesh>
      );
    case 'crystal':
      return (
        <group>
          <mesh>
            <octahedronGeometry args={[0.85, 0]} />
            <meshPhysicalMaterial 
              color={theme.color} emissive={theme.color} emissiveIntensity={emissiveIntensity * 0.4}
              roughness={0.1} metalness={0.8} transmission={0.9} thickness={1} flatShading
            />
          </mesh>
          <mesh scale={0.65}>
            <octahedronGeometry args={[1, 0]} />
            <meshBasicMaterial color={theme.ring} wireframe />
          </mesh>
        </group>
      );
    case 'hologram':
      return (
        <group>
          <mesh>
            <sphereGeometry args={[0.85, 16, 16]} />
            <meshStandardMaterial 
              color={theme.color} emissive={theme.color} emissiveIntensity={isSelected ? 3 : 1.5}
              wireframe roughness={0.1} metalness={0.1}
            />
          </mesh>
          <mesh scale={0.35}>
            <icosahedronGeometry args={[1, 0]} />
            <meshStandardMaterial color={theme.ring} emissive={theme.ring} emissiveIntensity={2} />
          </mesh>
        </group>
      );
    case 'energy':
      return (
        <mesh>
          <torusKnotGeometry args={[0.55, 0.18, 128, 32]} />
          <MeshWobbleMaterial 
            color={theme.color} emissive={theme.color} emissiveIntensity={emissiveIntensity * 1.5}
            factor={2} speed={3} roughness={0.2} metalness={0.8}
          />
        </mesh>
      );
    case 'glass':
      return (
        <group>
          <mesh>
            <sphereGeometry args={[0.75, 32, 32]} />
            <meshPhysicalMaterial 
              color={theme.color} emissive={theme.color} emissiveIntensity={emissiveIntensity * 0.8}
              roughness={0.05} metalness={0.1} transmission={0.9} ior={1.5} clearcoat={1}
            />
          </mesh>
          <mesh rotation={[Math.PI/4, 0, 0]}>
            <torusGeometry args={[0.95, 0.02, 32, 64]} />
            <meshBasicMaterial color={theme.ring} />
          </mesh>
          <mesh rotation={[-Math.PI/4, Math.PI/2, 0]}>
            <torusGeometry args={[0.95, 0.02, 32, 64]} />
            <meshBasicMaterial color={theme.color} />
          </mesh>
        </group>
      );
    default:
      return (
        <mesh>
          <icosahedronGeometry args={[0.85, 2]} />
          <meshStandardMaterial 
            color={theme.color} emissive={theme.color} emissiveIntensity={emissiveIntensity} 
            metalness={0.5} roughness={0.15}
          />
        </mesh>
      );
  }
}

export default function SkillStation({ course, position, courseIndex, onSelect, isSelected }) {
  const groupRef  = useRef();
  const coreRef   = useRef();
  const ring1Ref  = useRef();
  const ring2Ref  = useRef();

  const theme = COURSE_THEMES[courseIndex % COURSE_THEMES.length];
  const icon  = COURSE_ICONS[courseIndex % COURSE_ICONS.length];

  useFrame((state) => {
    const t = state.clock.elapsedTime;
    if (groupRef.current) {
      groupRef.current.position.y = position[1] + Math.sin(t * 0.35 + courseIndex * 1.5) * 0.18;
    }
    if (coreRef.current) {
      coreRef.current.rotation.y = t * 0.25 + courseIndex;
    }
    if (ring1Ref.current) {
      ring1Ref.current.rotation.z = t * 0.45 + courseIndex;
      ring1Ref.current.rotation.x = Math.PI / 2 + Math.sin(t * 0.12) * 0.1;
    }
    if (ring2Ref.current) {
      ring2Ref.current.rotation.z = -t * 0.3 + courseIndex;
      ring2Ref.current.rotation.x = Math.PI / 3 + Math.cos(t * 0.1) * 0.08;
    }
  });

  return (
    <group ref={groupRef} position={position}>
      {/* Glow halo */}
      <mesh>
        <sphereGeometry args={[1.2, 16, 16]} />
        <meshBasicMaterial color={theme.color} transparent opacity={isSelected ? 0.22 : 0.07} depthWrite={false} />
      </mesh>

      {/* Orbital ring 1 */}
      <mesh ref={ring1Ref} rotation={[Math.PI / 2, 0, 0]}>
        <torusGeometry args={[1.5, 0.045, 12, 64]} />
        <meshStandardMaterial color={theme.color} emissive={theme.color} emissiveIntensity={1.5} transparent opacity={0.75} />
      </mesh>

      {/* Orbital ring 2 */}
      <mesh ref={ring2Ref} rotation={[Math.PI / 3, 0, 0]}>
        <torusGeometry args={[1.75, 0.022, 8, 48]} />
        <meshStandardMaterial color={theme.ring} emissive={theme.ring} emissiveIntensity={0.9} transparent opacity={0.4} />
      </mesh>

      {/* Planet core — clickable */}
      <group
        ref={coreRef}
        onClick={(e) => { e.stopPropagation(); onSelect(course); }}
        onPointerOver={() => document.body.style.cursor = 'pointer'}
        onPointerOut={() => document.body.style.cursor = 'auto'}
      >
        <PlanetCore theme={theme} isSelected={isSelected} />

        <Html distanceFactor={13} position={[0, 1.65, 0]} center occlude={false} zIndexRange={[100, 0]} style={{ pointerEvents: 'none' }}>
          <div className="station-label" style={{ '--theme-color': theme.color }}>
            <span className="station-icon">{icon}</span>
            <span className="station-title">{course.name}</span>
            <span className="station-count">{course.materials.length} materiales</span>
            <span className="station-hint">← Clic para ver</span>
          </div>
        </Html>
      </group>
    </group>
  );
}
