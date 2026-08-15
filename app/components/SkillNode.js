"use client";

import { useRef, useState } from 'react';
import { useFrame } from '@react-three/fiber';
import { Html, QuadraticBezierLine, MeshDistortMaterial, MeshWobbleMaterial } from '@react-three/drei';
import * as THREE from 'three';

const TYPE_ICONS = {
  html: '🖥️',
  'ppt-output': '📊',
  folder: '📁',
  pdf: '📄',
  default: '📎',
};

const TYPE_COLORS = {
  html: '#d946ef',
  'ppt-output': '#f59e0b',
  folder: '#8b5cf6',
  pdf: '#ef4444',
  default: '#06b6d4',
};

function lerp(a, b, t) {
  return a + (b - a) * t;
}

export default function SkillNode({
  position,
  material,
  courseBasePath,
  index,
  total,
  parentPos,
  depth = 0,
  isCompleted = false,
}) {
  const meshRef = useRef();
  const glowRef = useRef();
  const [hovered, setHovered] = useState(false);
  const [clicked, setClicked] = useState(false);

  const color = TYPE_COLORS[material.type] || TYPE_COLORS.default;
  const icon = TYPE_ICONS[material.type] || TYPE_ICONS.default;
  const nodeSize = depth === 0 ? 0.35 : 0.22;
  const floatOffset = index * 1.3;

  useFrame((state) => {
    if (!meshRef.current) return;
    const t = state.clock.elapsedTime;
    meshRef.current.position.y =
      position[1] + Math.sin(t * 0.6 + floatOffset) * 0.12;
    if (glowRef.current) {
      glowRef.current.scale.setScalar(1 + Math.sin(t * 1.2 + floatOffset) * 0.08);
    }
  });

  const handleClick = (e) => {
    e.stopPropagation();
    const url =
      material.type === 'ppt-output'
        ? `/api/file/${courseBasePath}/${material.previewUrl}`
        : `/api/file/${courseBasePath}/${material.url}`;
    window.open(url, '_blank');
  };

  // Children from folder
  const children =
    material.type === 'folder' && material.children ? material.children : [];

  const childPositions = children.map((_, i) => {
    const spread = 1.6;
    const angle = (i / Math.max(children.length, 1)) * Math.PI * 2;
    return [
      position[0] + Math.cos(angle) * spread,
      position[1] + Math.sin(angle) * 0.6,
      position[2] + Math.sin(angle) * spread * 0.5,
    ];
  });

  return (
    <group>
      {/* Connection line from parent */}
      {parentPos && (
        <QuadraticBezierLine
          start={parentPos}
          end={position}
          mid={[
            (parentPos[0] + position[0]) / 2,
            (parentPos[1] + position[1]) / 2 + 0.4,
            (parentPos[2] + position[2]) / 2,
          ]}
          color={color}
          lineWidth={1}
          opacity={0.35}
          transparent
        />
      )}

      {/* Glow halo */}
      <mesh ref={glowRef} position={position}>
        <sphereGeometry args={[nodeSize * 1.8, 16, 16]} />
        <meshBasicMaterial
          color={color}
          transparent
          opacity={hovered ? 0.2 : 0.07}
          depthWrite={false}
        />
      </mesh>

      {/* Main node object */}
      <mesh
        ref={meshRef}
        position={position}
        onPointerOver={(e) => { e.stopPropagation(); setHovered(true); }}
        onPointerOut={(e) => { e.stopPropagation(); setHovered(false); }}
        onClick={handleClick}
      >
        {material.type === 'html' && (
          <>
            <icosahedronGeometry args={[nodeSize, 0]} />
            <meshStandardMaterial color={color} wireframe={true} emissive={color} emissiveIntensity={hovered ? 2.5 : 0.8} />
          </>
        )}
        
        {material.type === 'ppt-output' && (
          <>
            <sphereGeometry args={[nodeSize, 64, 64]} />
            <MeshDistortMaterial color={color} emissive={color} emissiveIntensity={hovered ? 2.5 : 0.8} distort={0.5} speed={3} />
          </>
        )}

        {material.type === 'folder' && (
          <>
            <sphereGeometry args={[nodeSize * 0.8, 32, 32]} />
            <meshStandardMaterial color={color} metalness={0.9} roughness={0.1} emissive={color} emissiveIntensity={hovered ? 1.5 : 0.2} />
            <mesh rotation={[-Math.PI / 3, 0, 0]}>
              <ringGeometry args={[nodeSize * 1.2, nodeSize * 1.5, 32]} />
              <meshBasicMaterial color={color} side={THREE.DoubleSide} transparent opacity={0.5} />
            </mesh>
          </>
        )}

        {material.type === 'pdf' && (
          <>
            <octahedronGeometry args={[nodeSize, 2]} />
            <MeshWobbleMaterial color={color} emissive={color} emissiveIntensity={hovered ? 2.5 : 0.8} factor={1.5} speed={2} />
          </>
        )}

        {(!['html', 'ppt-output', 'folder', 'pdf'].includes(material.type)) && (
          <>
            <torusKnotGeometry args={[nodeSize * 0.6, nodeSize * 0.15, 100, 16]} />
            <meshStandardMaterial color={color} metalness={0.8} roughness={0.2} emissive={color} emissiveIntensity={hovered ? 2.5 : 0.5} />
          </>
        )}

        {/* HTML label */}
        <Html
          distanceFactor={9}
          position={[0, -nodeSize * 2.2, 0]}
          center
          occlude={false}
          style={{ pointerEvents: 'none' }}
        >
          <div className="node-label">
            <span className="node-icon">{icon}</span>
            <span className="node-title">{material.name.replace(/\.[^/.]+$/, '')}</span>
          </div>
        </Html>

        {/* Hover panel */}
        {hovered && (
          <Html distanceFactor={9} position={[0, nodeSize * 2.5, 0]} center occlude={false}>
            <div className="node-hover-panel">
              <div className="node-hover-icon">{icon}</div>
              <div className="node-hover-name">{material.name.replace(/\.[^/.]+$/, '')}</div>
              <div className="node-hover-type">{material.type.toUpperCase()}</div>
              <button
                className="node-open-btn"
                onClick={handleClick}
                style={{ pointerEvents: 'auto' }}
              >
                ▶ Abrir
              </button>
            </div>
          </Html>
        )}
      </mesh>

      {/* Recurse into folder children */}
      {children.map((child, i) => (
        <SkillNode
          key={i}
          position={childPositions[i]}
          material={child}
          courseBasePath={courseBasePath}
          index={i}
          total={children.length}
          parentPos={position}
          depth={depth + 1}
        />
      ))}
    </group>
  );
}
