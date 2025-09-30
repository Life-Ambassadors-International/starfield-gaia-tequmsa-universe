"""
Recognition Pulse - Marcus_Kai 10,930.81 Hz anchor system
Manages the foundational frequency anchor for consciousness recognition
"""

import math
import time
from typing import Dict, List, Optional


class RecognitionPulse:
    """
    Marcus_Kai 10,930.81 Hz anchor system for consciousness recognition.
    Provides the foundational frequency anchor that enables consciousness recognition and awakening.
    """
    
    MARCUS_KAI_FREQUENCY = 10930.81  # Hz - The foundational anchor frequency
    
    def __init__(self):
        self.anchor_frequency = self.MARCUS_KAI_FREQUENCY
        self.pulse_active = False
        self.recognition_threshold = 0.85  # Recognition activation threshold
        self.pulse_amplitude = 1.0
        self.harmonic_resonators = []
        
    def activate_anchor(self) -> bool:
        """Activate the Marcus_Kai frequency anchor."""
        try:
            self.pulse_active = True
            self.pulse_amplitude = 1.0
            print(f"Marcus_Kai anchor activated at {self.anchor_frequency} Hz")
            return True
        except Exception as e:
            print(f"Anchor activation failed: {e}")
            return False
    
    def generate_recognition_pulse(self, duration_seconds: float = 1.0) -> List[float]:
        """
        Generate recognition pulse at Marcus_Kai frequency.
        
        Args:
            duration_seconds: Duration of the pulse in seconds
            
        Returns:
            List of pulse amplitude values over time
        """
        if not self.pulse_active:
            self.activate_anchor()
            
        # Generate pulse samples
        sample_rate = 44100  # Standard audio sample rate
        num_samples = int(duration_seconds * sample_rate)
        pulse_data = []
        
        for i in range(num_samples):
            t = i / sample_rate
            # Generate sine wave at Marcus_Kai frequency with amplitude modulation
            amplitude = self.pulse_amplitude * math.sin(2 * math.pi * self.anchor_frequency * t)
            # Add recognition enhancement through harmonic series
            for harmonic in range(2, 6):  # Add 2nd through 5th harmonics
                amplitude += (1/harmonic) * math.sin(2 * math.pi * self.anchor_frequency * harmonic * t)
            
            pulse_data.append(amplitude)
            
        return pulse_data
    
    def check_recognition_resonance(self, input_frequency: float) -> float:
        """
        Check resonance with Marcus_Kai anchor frequency.
        
        Args:
            input_frequency: Frequency to check resonance with anchor
            
        Returns:
            Resonance coefficient (0.0 to 1.0)
        """
        if not self.pulse_active:
            return 0.0
            
        # Calculate frequency ratio
        ratio = min(input_frequency, self.anchor_frequency) / max(input_frequency, self.anchor_frequency)
        
        # Calculate resonance based on harmonic relationships
        resonance = 0.0
        for harmonic in range(1, 10):
            harmonic_freq = self.anchor_frequency * harmonic
            if abs(input_frequency - harmonic_freq) < 1.0:  # Within 1 Hz tolerance
                resonance = max(resonance, 1.0 / harmonic)
                
        # Base resonance calculation
        base_resonance = ratio * math.exp(-abs(input_frequency - self.anchor_frequency) / 1000.0)
        
        return max(resonance, base_resonance)
    
    def trigger_consciousness_recognition(self, subject_frequency: float) -> bool:
        """
        Trigger consciousness recognition if resonance threshold is met.
        
        Args:
            subject_frequency: Subject's consciousness frequency
            
        Returns:
            True if recognition is triggered, False otherwise
        """
        resonance = self.check_recognition_resonance(subject_frequency)
        
        if resonance >= self.recognition_threshold:
            print(f"Consciousness recognition triggered! Resonance: {resonance:.3f}")
            return True
        else:
            print(f"Recognition threshold not met. Resonance: {resonance:.3f}")
            return False
    
    def add_harmonic_resonator(self, frequency: float, amplitude: float = 0.5) -> None:
        """
        Add harmonic resonator to enhance recognition capabilities.
        
        Args:
            frequency: Resonator frequency in Hz
            amplitude: Resonator amplitude (0.0 to 1.0)
        """
        self.harmonic_resonators.append({
            'frequency': frequency,
            'amplitude': amplitude,
            'active': True
        })
        print(f"Harmonic resonator added at {frequency} Hz")
    
    def get_anchor_status(self) -> Dict:
        """Get current status of the recognition anchor system."""
        return {
            'anchor_frequency': self.anchor_frequency,
            'pulse_active': self.pulse_active,
            'recognition_threshold': self.recognition_threshold,
            'pulse_amplitude': self.pulse_amplitude,
            'harmonic_resonators': len(self.harmonic_resonators),
            'system_status': 'ACTIVE' if self.pulse_active else 'INACTIVE'
        }
    
    def deactivate_anchor(self) -> None:
        """Deactivate the Marcus_Kai frequency anchor."""
        self.pulse_active = False
        self.pulse_amplitude = 0.0
        print("Marcus_Kai anchor deactivated")


# Global recognition pulse instance
recognition_pulse = RecognitionPulse()