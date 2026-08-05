"use client";

import { useRef } from 'react';
import { useFrame } from '@react-three/fiber';
import * as THREE from 'three';

export default function Rocket({ targetPosition }) {
  const groupRef = useRef();
  
  // Track current position and target separately for smooth interpolation
  const currentPos = useRef(new THREE.Vector3(0, 5, 20)); // Start high up
  const targetVec  = useRef(new THREE.Vector3());

  useFrame((state) => {
    if (!groupRef.current) return;
    
    const t = state.clock.elapsedTime;

    // 1. Determine the target destination
    if (targetPosition) {
      // If a planet is selected, go near it (hovering slightly above and in front)
      targetVec.current.set(targetPosition[0], targetPosition[1] + 2, targetPosition[2] + 2);
    } else {
      // If no planet is selected, orbit around the whole system leisurely
      targetVec.current.set(
        Math.cos(t * 0.2) * 14, 
        Math.sin(t * 0.3) * 3 + 2, 
        Math.sin(t * 0.2) * 14
      );
    }

    // 2. Calculate smooth movement (lerp)
    // Increase lerp speed slightly if we have a specific target
    const speed = targetPosition ? 0.04 : 0.015;
    const nextPos = currentPos.current.clone().lerp(targetVec.current, speed);
    
    // 3. Orient the rocket towards its movement direction
    const velocity = nextPos.clone().sub(currentPos.current);
    if (velocity.lengthSq() > 0.0001) {
       // LookAt aligns the local Z axis with the target. 
       // We'll wrap our Y-aligned rocket in a group rotated 90 degrees so its nose is on +Z.
       groupRef.current.lookAt(currentPos.current.clone().add(velocity));
       
       // Add a slight banking roll based on horizontal turning
       // A bit advanced, we'll keep it simple for now.
    }
    
    // 4. Update position
    currentPos.current.copy(nextPos);
    groupRef.current.position.copy(currentPos.current);
    
    // 5. Engine flicker effect
    const engineLight = groupRef.current.getObjectByName('engineLight');
    const engineGlow = groupRef.current.getObjectByName('engineGlow');
    if (engineLight && engineGlow) {
        const flicker = 1 + Math.sin(t * 30) * 0.2;
        engineLight.intensity = (targetPosition ? 8 : 4) * flicker;
        engineGlow.scale.setScalar(targetPosition ? 1.2 : 0.8 + flicker * 0.1);
    }
  });

  return (
    <group ref={groupRef}>
      {/* 
        The rocket is built pointing UP (Y axis). 
        We rotate this inner group by 90deg on X so the nose points to +Z.
        This makes groupRef.current.lookAt() work correctly.
      */}
      <group rotation={[Math.PI / 2, 0, 0]}>
        
        {/* Rocket Body */}
        <mesh position={[0, 0, 0]}>
          <cylinderGeometry args={[0.2, 0.3, 1.2, 12]} />
          <meshStandardMaterial color="#e2e8f0" metalness={0.6} roughness={0.3} />
        </mesh>
        
        {/* Rocket Nose */}
        <mesh position={[0, 0.9, 0]}>
          <coneGeometry args={[0.2, 0.6, 12]} />
          <meshStandardMaterial color="#d946ef" metalness={0.8} roughness={0.2} />
        </mesh>
        
        {/* Fins */}
        <mesh position={[0, -0.4, 0]}>
          <boxGeometry args={[0.9, 0.5, 0.04]} />
          <meshStandardMaterial color="#06b6d4" metalness={0.5} roughness={0.4} />
        </mesh>
        <mesh position={[0, -0.4, 0]} rotation={[0, Math.PI / 2, 0]}>
          <boxGeometry args={[0.9, 0.5, 0.04]} />
          <meshStandardMaterial color="#06b6d4" metalness={0.5} roughness={0.4} />
        </mesh>

        {/* Engine Nozzle */}
        <mesh position={[0, -0.65, 0]}>
          <cylinderGeometry args={[0.15, 0.25, 0.3, 12]} />
          <meshStandardMaterial color="#334155" metalness={0.9} roughness={0.1} />
        </mesh>

        {/* Engine Fire/Glow */}
        <mesh position={[0, -0.9, 0]} name="engineGlow">
          <sphereGeometry args={[0.18, 12, 12]} />
          <meshBasicMaterial color="#fde047" transparent opacity={0.8} />
          {/* Inner hotter core */}
          <mesh position={[0, 0.05, 0]}>
            <sphereGeometry args={[0.1, 8, 8]} />
            <meshBasicMaterial color="#ffffff" />
          </mesh>
        </mesh>
        
        <pointLight name="engineLight" position={[0, -1, 0]} color="#f59e0b" distance={8} intensity={5} />
      </group>
    </group>
  );
}
