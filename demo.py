#!/usr/bin/env python3
"""
Quick Demo Script for Voice Cloning App
Demonstrates the text-to-speech capabilities with various voices
"""

from voice_app import VoiceApp
import time

def demo():
    """Run a demonstration of the voice app"""
    app = VoiceApp()
    
    print("\n" + "="*70)
    print("VOICE CLONING & TEXT-TO-SPEECH APP - DEMO")
    print("="*70)
    
    demo_text = "Hello! I'm a voice from the voice cloning app. I can speak with different accents and styles."
    
    print("\n📝 Demo Text:")
    print(f'"{demo_text}"')
    print("\n" + "-"*70)
    
    # Demo 1: US Female Voice (Google TTS)
    print("\n🎤 Demo 1: US Female Voice (Google TTS)")
    print("Generating...")
    app.text_to_speech_gtts(demo_text, tld='com', filename="demo_us_female.mp3")
    time.sleep(1)
    
    # Demo 2: UK Female Voice (Google TTS)
    print("\n🎤 Demo 2: UK Female Voice (Google TTS)")
    print("Generating...")
    app.text_to_speech_gtts(demo_text, tld='co.uk', filename="demo_uk_female.mp3")
    time.sleep(1)
    
    # Demo 3: Australian Female Voice (Google TTS)
    print("\n🎤 Demo 3: Australian Female Voice (Google TTS)")
    print("Generating...")
    app.text_to_speech_gtts(demo_text, tld='com.au', filename="demo_au_female.mp3")
    time.sleep(1)
    
    # Demo 4: System Voice
    print("\n🎤 Demo 4: System Voice")
    if app.available_voices:
        print("Generating...")
        app.text_to_speech_pyttsx3(demo_text, voice_id=0, filename="demo_system.wav")
    else:
        print("No system voices available")
    
    print("\n" + "="*70)
    print("✅ DEMO COMPLETE!")
    print("="*70)
    print("\n📁 Generated files can be found in the 'output/' directory")
    print("\nFiles created:")
    print("  - demo_us_female.mp3 (US Female Voice)")
    print("  - demo_uk_female.mp3 (UK Female Voice)")
    print("  - demo_au_female.mp3 (Australian Female Voice)")
    if app.available_voices:
        print("  - demo_system.wav (System Voice)")
    print("\n🎧 You can now play these files to hear the different voices!")
    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    demo()
