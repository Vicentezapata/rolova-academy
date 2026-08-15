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
      targetVec.current.set(targetPosition[0], targetPosition[1] + 3, targetPosition[2] + 3);
    } else {
      // If no planet is selected, orbit around the whole system leisurely
      targetVec.current.set(
        Math.cos(t * 0.3) * 10, 
        Math.sin(t * 0.4) * 2 + 2, 
        Math.sin(t * 0.3) * 10
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
    const engineGlow1 = groupRef.current.getObjectByName('engineGlow1');
    const engineGlow2 = groupRef.current.getObjectByName('engineGlow2');
    
    if (engineLight) {
        const flicker = 1 + Math.sin(t * 30) * 0.2;
        engineLight.intensity = (targetPosition ? 10 : 5) * flicker;
        const s = targetPosition ? 1.3 : 0.9 + flicker * 0.1;
        if (engineGlow1) engineGlow1.scale.setScalar(s);
        if (engineGlow2) engineGlow2.scale.setScalar(s);
    }
  });

  return (
    <group ref={groupRef}>
      {/* 
        The rocket is built pointing UP (Y axis). 
        We rotate this inner group by 90deg on X so the nose points to +Z.
        This makes groupRef.current.lookAt() work correctly.
      */}
      <group rotation={[Math.PI / 2, 0, 0]} scale={[2.2, 2.2, 2.2]}>
        
        {/* Main Fuselage (Sleek dark wedge) */}
        <mesh position={[0, 0, 0]} scale={[0.4, 1, 0.25]}>
          <cylinderGeometry args={[0, 0.8, 2, 4]} />
          <meshStandardMaterial color="#0f172a" metalness={0.9} roughness={0.2} />
        </mesh>
        
        {/* Glowing Cockpit Canopy */}
        <mesh position={[0, 0.2, 0.1]} scale={[0.2, 0.5, 0.15]}>
          <cylinderGeometry args={[0, 0.8, 1, 4]} />
          <meshStandardMaterial color="#0ea5e9" metalness={0.9} roughness={0.1} emissive="#0284c7" emissiveIntensity={1} />
        </mesh>

        {/* Delta Wings */}
        <mesh position={[0, -0.3, -0.05]} scale={[1.8, 0.8, 0.05]} rotation={[0, Math.PI / 4, 0]}>
          {/* 4-sided cylinder rotated 45deg = wide diamond */}
          <cylinderGeometry args={[0, 0.8, 1.2, 4]} />
          <meshStandardMaterial color="#1e293b" metalness={0.9} roughness={0.3} />
        </mesh>

        {/* Wing Cannons / Sensors */}
        <mesh position={[-1.2, -0.5, -0.05]}>
          <cylinderGeometry args={[0.02, 0.02, 0.8, 8]} />
          <meshStandardMaterial color="#94a3b8" metalness={1} roughness={0.1} />
        </mesh>
        <mesh position={[1.2, -0.5, -0.05]}>
          <cylinderGeometry args={[0.02, 0.02, 0.8, 8]} />
          <meshStandardMaterial color="#94a3b8" metalness={1} roughness={0.1} />
        </mesh>

        {/* Twin Ion Engines */}
        <mesh position={[-0.25, -0.9, 0]}>
          <cylinderGeometry args={[0.08, 0.12, 0.3, 12]} />
          <meshStandardMaterial color="#334155" metalness={0.9} roughness={0.2} />
        </mesh>
        <mesh position={[0.25, -0.9, 0]}>
          <cylinderGeometry args={[0.08, 0.12, 0.3, 12]} />
          <meshStandardMaterial color="#334155" metalness={0.9} roughness={0.2} />
        </mesh>

        {/* Engine Ion Glows (Blue/Cyan) */}
        <mesh position={[-0.25, -1.15, 0]} name="engineGlow1">
          <capsuleGeometry args={[0.06, 0.2, 4, 8]} />
          <meshBasicMaterial color="#06b6d4" transparent opacity={0.9} />
        </mesh>
        <mesh position={[0.25, -1.15, 0]} name="engineGlow2">
          <capsuleGeometry args={[0.06, 0.2, 4, 8]} />
          <meshBasicMaterial color="#06b6d4" transparent opacity={0.9} />
        </mesh>

        <pointLight name="engineLight" position={[0, -1.5, 0]} color="#06b6d4" distance={20} intensity={10} />
      </group>
    </group>
  );
}
