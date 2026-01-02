#!/usr/bin/env python3
"""
Advanced Voice Cloning Module
Uses Coqui TTS for high-quality voice cloning and synthesis
"""

import os
import sys
from pathlib import Path

try:
    from TTS.api import TTS
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("Warning: Coqui TTS not installed. Advanced voice cloning features disabled.")

class VoiceCloner:
    """Advanced voice cloning using Coqui TTS"""
    
    def __init__(self):
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        self.model = None
        
        if TTS_AVAILABLE:
            try:
                # Initialize with a multi-speaker model
                print("Loading TTS model... This may take a moment on first run.")
                # Use VCTK model which has multiple speakers including female voices
                self.model = TTS(model_name="tts_models/en/vctk/vits", progress_bar=True)
                self.speakers = self.model.speakers if hasattr(self.model, 'speakers') else []
                print(f"✓ TTS model loaded successfully with {len(self.speakers)} speakers")
            except Exception as e:
                print(f"✗ Error loading TTS model: {e}")
                self.model = None
    
    def list_speakers(self):
        """List all available speakers in the model"""
        if not TTS_AVAILABLE or not self.model:
            print("✗ TTS model not available")
            return []
        
        if not self.speakers:
            print("No multi-speaker support in current model")
            return []
        
        print("\n" + "="*60)
        print("AVAILABLE SPEAKERS (Coqui TTS)")
        print("="*60)
        
        # Filter and highlight female speakers
        female_indicators = ['f_', 'female', 'woman', 'lady', 'p2', 'p3', 'p4']
        
        for idx, speaker in enumerate(self.speakers):
            speaker_lower = speaker.lower()
            is_female = any(indicator in speaker_lower for indicator in female_indicators)
            marker = "★" if is_female else " "
            print(f"{marker} {idx}: {speaker}")
        
        print("\n★ = Likely female voice")
        print("="*60 + "\n")
        return self.speakers
    
    def synthesize_speech(self, text, speaker_idx=None, filename="cloned_output.wav"):
        """Generate speech with specified speaker"""
        if not TTS_AVAILABLE or not self.model:
            print("✗ TTS model not available")
            return None
        
        try:
            output_path = self.output_dir / filename
            
            if self.speakers and speaker_idx is not None:
                if 0 <= speaker_idx < len(self.speakers):
                    speaker = self.speakers[speaker_idx]
                    print(f"Using speaker: {speaker}")
                    self.model.tts_to_file(
                        text=text,
                        speaker=speaker,
                        file_path=str(output_path)
                    )
                else:
                    print(f"✗ Invalid speaker index. Must be 0-{len(self.speakers)-1}")
                    return None
            else:
                # Use default speaker
                self.model.tts_to_file(text=text, file_path=str(output_path))
            
            print(f"✓ Audio saved to: {output_path}")
            return str(output_path)
        
        except Exception as e:
            print(f"✗ Error generating speech: {e}")
            return None
    
    def clone_voice_from_file(self, text, reference_audio_path, filename="voice_cloned.wav"):
        """
        Clone a voice from a reference audio file
        Note: This requires a model that supports voice cloning from audio
        """
        if not TTS_AVAILABLE:
            print("✗ TTS not available")
            return None
        
        try:
            # Try to load a voice conversion model
            print("Attempting voice cloning from reference audio...")
            vc_model = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24")
            
            output_path = self.output_dir / filename
            vc_model.voice_conversion_to_file(
                source_wav=reference_audio_path,
                target_wav=reference_audio_path,
                file_path=str(output_path)
            )
            
            print(f"✓ Voice cloned to: {output_path}")
            return str(output_path)
        
        except Exception as e:
            print(f"✗ Voice cloning failed: {e}")
            print("Note: Voice cloning from audio requires specific models and reference audio.")
            return None

def main():
    """Test the voice cloner"""
    cloner = VoiceCloner()
    
    if not TTS_AVAILABLE or not cloner.model:
        print("Please install TTS: pip install TTS")
        return
    
    print("\n" + "="*60)
    print("ADVANCED VOICE CLONING MODULE")
    print("="*60)
    
    while True:
        print("\nVoice Cloning Menu:")
        print("1. List available speakers")
        print("2. Synthesize speech with selected speaker")
        print("3. Quick synthesis (default speaker)")
        print("4. Return to main menu")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            cloner.list_speakers()
        
        elif choice == '2':
            cloner.list_speakers()
            speaker_idx = input("\nEnter speaker number: ").strip()
            try:
                speaker_idx = int(speaker_idx)
            except ValueError:
                print("✗ Invalid speaker number")
                continue
            
            text = input("\nEnter text to synthesize: ").strip()
            if not text:
                print("✗ Text cannot be empty")
                continue
            
            print("\nSynthesizing...")
            cloner.synthesize_speech(text, speaker_idx)
        
        elif choice == '3':
            text = input("\nEnter text to synthesize: ").strip()
            if not text:
                print("✗ Text cannot be empty")
                continue
            
            print("\nSynthesizing with default speaker...")
            cloner.synthesize_speech(text)
        
        elif choice == '4':
            break
        
        else:
            print("✗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
