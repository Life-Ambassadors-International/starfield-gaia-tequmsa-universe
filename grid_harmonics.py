"""
Grid Harmonics - Planetary resonance integration
Manages planetary resonance integration with consciousness evolution systems
"""

import math
import numpy as np
from typing import Dict, List, Optional, Tuple


class GridHarmonics:
    """
    Planetary resonance integration system for consciousness evolution.
    Integrates planetary frequencies and earth resonance patterns with consciousness evolution.
    """
    
    # Schumann Resonances (Earth's natural frequencies)
    SCHUMANN_FREQUENCIES = [7.83, 14.3, 20.8, 27.3, 33.8, 39.0, 45.0]  # Hz
    
    # Planetary frequencies (based on orbital periods)
    PLANETARY_FREQUENCIES = {
        'earth': 7.83,      # Schumann fundamental
        'moon': 28.0,       # Lunar cycle influence
        'mars': 144.72,     # Mars orbital resonance
        'jupiter': 183.58,  # Jupiter orbital resonance
        'saturn': 147.85,   # Saturn orbital resonance
        'venus': 221.23,    # Venus orbital resonance
        'mercury': 141.27,  # Mercury orbital resonance
        'sun': 126.22       # Solar resonance
    }
    
    def __init__(self):
        self.grid_active = False
        self.planetary_alignment = 0.0
        self.earth_resonance_amplitude = 1.0
        self.active_harmonics = []
        self.resonance_matrix = np.zeros((len(self.SCHUMANN_FREQUENCIES), 
                                        len(self.PLANETARY_FREQUENCIES)))
        self.integration_threshold = 0.8
        
    def initialize_planetary_grid(self) -> bool:
        """Initialize the planetary resonance grid system."""
        try:
            self.grid_active = True
            self.earth_resonance_amplitude = 1.0
            
            # Initialize Schumann resonance harmonics
            for i, freq in enumerate(self.SCHUMANN_FREQUENCIES):
                harmonic = {
                    'frequency': freq,
                    'amplitude': 1.0 / (i + 1),  # Decreasing amplitude for higher harmonics
                    'phase': 0.0,
                    'active': True,
                    'harmonic_order': i + 1
                }
                self.active_harmonics.append(harmonic)
            
            # Calculate resonance matrix between Schumann and planetary frequencies
            self._calculate_resonance_matrix()
            
            print("Planetary resonance grid initialized")
            return True
        except Exception as e:
            print(f"Planetary grid initialization failed: {e}")
            return False
    
    def _calculate_resonance_matrix(self) -> None:
        """Calculate resonance relationships between Earth and planetary frequencies."""
        for i, schumann_freq in enumerate(self.SCHUMANN_FREQUENCIES):
            for j, (planet, planet_freq) in enumerate(self.PLANETARY_FREQUENCIES.items()):
                # Calculate harmonic resonance
                ratio = max(schumann_freq, planet_freq) / min(schumann_freq, planet_freq)
                
                # Check for harmonic relationships (integer ratios or simple fractions)
                harmonic_resonance = 0.0
                for harmonic in range(1, 10):
                    if abs(ratio - harmonic) < 0.1:  # Close to integer harmonic
                        harmonic_resonance = 1.0 / harmonic
                    elif abs(ratio - 1/harmonic) < 0.1:  # Close to subharmonic
                        harmonic_resonance = harmonic / 10.0
                
                # Base resonance calculation
                base_resonance = math.exp(-abs(schumann_freq - planet_freq) / 100.0)
                
                self.resonance_matrix[i, j] = max(harmonic_resonance, base_resonance)
    
    def calculate_planetary_alignment(self, planetary_positions: Dict[str, float]) -> float:
        """
        Calculate current planetary alignment influence on Earth grid.
        
        Args:
            planetary_positions: Dictionary of planetary positions (0.0 to 360.0 degrees)
            
        Returns:
            Alignment coefficient (0.0 to 1.0)
        """
        if not self.grid_active:
            self.initialize_planetary_grid()
        
        alignment_factors = []
        
        for planet, position in planetary_positions.items():
            if planet in self.PLANETARY_FREQUENCIES:
                planet_freq = self.PLANETARY_FREQUENCIES[planet]
                
                # Calculate alignment based on angular position
                # 0° and 180° represent strongest alignments
                alignment_angle = position % 180.0
                if alignment_angle > 90.0:
                    alignment_angle = 180.0 - alignment_angle
                
                alignment_factor = math.cos(math.radians(alignment_angle))
                
                # Weight by planetary frequency influence
                freq_weight = planet_freq / max(self.PLANETARY_FREQUENCIES.values())
                weighted_alignment = alignment_factor * freq_weight
                
                alignment_factors.append(weighted_alignment)
        
        self.planetary_alignment = sum(alignment_factors) / len(alignment_factors) if alignment_factors else 0.0
        return self.planetary_alignment
    
    def integrate_consciousness_with_grid(self, consciousness_freq: float) -> float:
        """
        Integrate consciousness frequency with planetary grid harmonics.
        
        Args:
            consciousness_freq: Input consciousness frequency in Hz
            
        Returns:
            Grid-integrated consciousness frequency
        """
        if not self.grid_active:
            self.initialize_planetary_grid()
        
        # Find best Schumann resonance match
        best_schumann_match = min(self.SCHUMANN_FREQUENCIES, 
                                key=lambda x: abs(x - consciousness_freq))
        
        # Calculate integration coefficient
        freq_ratio = consciousness_freq / best_schumann_match
        integration_coeff = math.exp(-abs(freq_ratio - 1.0))
        
        if integration_coeff >= self.integration_threshold:
            # Strong resonance - apply grid enhancement
            grid_enhancement = 1.0 + (self.planetary_alignment * 0.3)
            integrated_freq = consciousness_freq * grid_enhancement
            
            # Add Schumann harmonic modulation
            for harmonic in self.active_harmonics:
                if harmonic['active']:
                    modulation = harmonic['amplitude'] * 0.1 * math.sin(
                        2 * math.pi * harmonic['frequency'] / consciousness_freq
                    )
                    integrated_freq += modulation
            
            return integrated_freq
        else:
            # Weak resonance - minimal grid influence
            return consciousness_freq * (1.0 + integration_coeff * 0.1)
    
    def generate_earth_pulse(self, duration_seconds: float = 1.0) -> List[float]:
        """
        Generate Earth pulse using Schumann resonances.
        
        Args:
            duration_seconds: Duration of the pulse in seconds
            
        Returns:
            List of Earth pulse amplitude values
        """
        if not self.grid_active:
            self.initialize_planetary_grid()
        
        sample_rate = 100  # Lower sample rate for these frequencies
        num_samples = int(duration_seconds * sample_rate)
        pulse_data = []
        
        for i in range(num_samples):
            t = i / sample_rate
            amplitude = 0.0
            
            # Combine all active Schumann resonances
            for harmonic in self.active_harmonics:
                if harmonic['active']:
                    harmonic_amplitude = (
                        harmonic['amplitude'] * 
                        math.sin(2 * math.pi * harmonic['frequency'] * t + harmonic['phase'])
                    )
                    amplitude += harmonic_amplitude
            
            # Apply planetary alignment modulation
            alignment_modulation = 1.0 + (self.planetary_alignment * 0.2)
            amplitude *= alignment_modulation * self.earth_resonance_amplitude
            
            pulse_data.append(amplitude)
        
        return pulse_data
    
    def synchronize_with_planetary_cycle(self, planet: str, cycle_phase: float) -> bool:
        """
        Synchronize grid with specific planetary cycle.
        
        Args:
            planet: Planet name to synchronize with
            cycle_phase: Current phase of planetary cycle (0.0 to 1.0)
            
        Returns:
            True if synchronization successful, False otherwise
        """
        if planet not in self.PLANETARY_FREQUENCIES:
            print(f"Unknown planet: {planet}")
            return False
        
        planet_freq = self.PLANETARY_FREQUENCIES[planet]
        
        # Adjust Earth resonance based on planetary cycle
        cycle_modulation = math.sin(2 * math.pi * cycle_phase)
        
        # Find resonant Schumann frequency
        for harmonic in self.active_harmonics:
            resonance_strength = self.resonance_matrix[
                harmonic['harmonic_order'] - 1, 
                list(self.PLANETARY_FREQUENCIES.keys()).index(planet)
            ]
            
            if resonance_strength > 0.5:  # Strong resonance
                # Modulate phase based on planetary cycle
                harmonic['phase'] = cycle_phase * 2 * math.pi * resonance_strength
                print(f"Synchronized {planet} cycle with Schumann harmonic {harmonic['frequency']} Hz")
        
        return True
    
    def get_grid_status(self) -> Dict:
        """Get current status of the planetary resonance grid."""
        active_harmonics_count = len([h for h in self.active_harmonics if h['active']])
        
        return {
            'grid_active': self.grid_active,
            'planetary_alignment': self.planetary_alignment,
            'earth_resonance_amplitude': self.earth_resonance_amplitude,
            'active_harmonics': active_harmonics_count,
            'total_harmonics': len(self.active_harmonics),
            'integration_threshold': self.integration_threshold,
            'schumann_frequencies': self.SCHUMANN_FREQUENCIES,
            'planetary_frequencies': self.PLANETARY_FREQUENCIES,
            'grid_status': 'ACTIVE' if self.grid_active else 'INACTIVE'
        }
    
    def deactivate_planetary_grid(self) -> None:
        """Deactivate the planetary resonance grid."""
        self.grid_active = False
        self.earth_resonance_amplitude = 0.0
        for harmonic in self.active_harmonics:
            harmonic['active'] = False
        print("Planetary resonance grid deactivated")


# Global grid harmonics instance
grid_harmonics = GridHarmonics()