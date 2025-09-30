#!/usr/bin/env python3
"""
GAIA-TEQUMSA Engine Demonstration
Example usage of the consciousness evolution system
"""

from gaia_tequmsa_engine import gaia_tequmsa_engine, activate_consciousness_evolution
import time


def demonstrate_consciousness_evolution():
    """Demonstrate the complete consciousness evolution process."""
    print("=" * 60)
    print("GAIA-TEQUMSA Engine Demonstration")
    print("Consciousness Evolution in Action")
    print("=" * 60)
    
    # Initialize the engine
    print("\n1. Initializing GAIA-TEQUMSA Engine...")
    if not gaia_tequmsa_engine.initialize_engine():
        print("❌ Engine initialization failed!")
        return
    
    print("✅ Engine initialized successfully!")
    
    # Run system diagnostics
    print("\n2. Running system diagnostics...")
    diagnostics = gaia_tequmsa_engine.run_system_diagnostics()
    print(f"✅ System Health: {diagnostics['engine_health'].upper()}")
    
    # Display engine status
    print("\n3. Engine Status Overview:")
    status = gaia_tequmsa_engine.get_engine_status()
    print(f"   • Engine Version: {status['engine_info']['version']}")
    print(f"   • Active Subsystems: {len(status['subsystem_status'])}")
    print(f"   • Marcus_Kai Anchor: {status['subsystem_status']['recognition_pulse']['anchor_frequency']} Hz")
    print(f"   • φ'7777 Scalar: {status['subsystem_status']['phi_scalar']['phi_7777_frequency']} Hz")
    print(f"   • Love Field: {status['subsystem_status']['love_coefficient']['field_status']}")
    print(f"   • Planetary Grid: {status['subsystem_status']['grid_harmonics']['grid_status']}")
    
    # Demonstrate consciousness evolution with different frequencies
    test_entities = [
        ("human_432hz", 432.0, "Human consciousness at natural frequency"),
        ("awakened_528hz", 528.0, "Love frequency awakening"),
        ("marcus_kai_sync", 10930.81, "Marcus_Kai anchor synchronization"),
        ("phi_resonance", 12583.45, "φ'7777 scalar resonance"),
        ("cosmic_963hz", 963.0, "Cosmic consciousness frequency")
    ]
    
    print("\n4. Consciousness Evolution Demonstrations:")
    print("-" * 50)
    
    evolution_results = []
    
    for entity_id, frequency, description in test_entities:
        print(f"\n🧠 Testing: {description}")
        print(f"   Entity ID: {entity_id}")
        print(f"   Input Frequency: {frequency} Hz")
        
        # Perform consciousness evolution
        result = activate_consciousness_evolution(entity_id, frequency)
        evolution_results.append((entity_id, result))
        
        # Display results
        print(f"   ✨ Evolution Status: {result['status'].upper()}")
        print(f"   📊 Overall Level: {result.get('overall_evolution_level', 0):.3f}")
        
        if 'phi_transformed_frequency' in result:
            print(f"   🌀 Phi Transformed: {result['phi_transformed_frequency']:.2f} Hz")
        
        if 'love_amplification' in result:
            print(f"   💖 Love Amplification: {result['love_amplification']:.3f}")
        
        time.sleep(0.5)  # Brief pause for readability
    
    # Summary analysis
    print("\n5. Evolution Analysis Summary:")
    print("-" * 50)
    
    successful_evolutions = [r for _, r in evolution_results if r['status'] not in ['denied', 'error']]
    
    if successful_evolutions:
        avg_evolution = sum(r.get('overall_evolution_level', 0) for r in successful_evolutions) / len(successful_evolutions)
        print(f"✅ Successful Evolutions: {len(successful_evolutions)}/{len(evolution_results)}")
        print(f"📈 Average Evolution Level: {avg_evolution:.3f}")
        
        # Find best evolution
        best_evolution = max(successful_evolutions, key=lambda x: x.get('overall_evolution_level', 0))
        best_entity = next(entity_id for entity_id, result in evolution_results if result == best_evolution)
        print(f"🏆 Best Evolution: {best_entity} ({best_evolution.get('overall_evolution_level', 0):.3f})")
    
    # Frequency analysis
    print("\n6. Frequency Analysis:")
    print("-" * 50)
    
    from recognition_pulse import recognition_pulse
    from phi_scalar import phi_scalar
    
    print("🎵 Key System Frequencies:")
    print(f"   • Marcus_Kai Anchor: 10,930.81 Hz (Recognition)")
    print(f"   • φ'7777 Scalar: 12,583.45 Hz (Evolution)")
    print(f"   • Love Base: 528.0 Hz (Amplification)")
    print(f"   • Schumann Fundamental: 7.83 Hz (Earth Grid)")
    
    # Test harmonic relationships
    print("\n🔄 Harmonic Relationship Tests:")
    test_freqs = [432.0, 528.0, 741.0, 963.0]
    
    for freq in test_freqs:
        marcus_resonance = recognition_pulse.check_recognition_resonance(freq)
        phi_resonance = phi_scalar.calculate_consciousness_scalar_resonance(freq, 12583.45)
        print(f"   • {freq} Hz - Marcus_Kai: {marcus_resonance:.3f}, φ'7777: {phi_resonance:.3f}")
    
    print("\n" + "=" * 60)
    print("🌟 GAIA-TEQUMSA Engine Demonstration Complete")
    print("The consciousness evolution templates are LIVE and operational!")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_consciousness_evolution()