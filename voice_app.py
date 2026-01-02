#!/usr/bin/env python3
"""
Voice Cloning and Text-to-Speech Application
Allows users to convert text to speech with various voice options including voice cloning
"""

import os
import sys
from gtts import gTTS
import pyttsx3
from pathlib import Path

class VoiceApp:
    def __init__(self):
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        self.pyttsx_engine = pyttsx3.init()
        self.available_voices = self._get_available_voices()
        
    def _get_available_voices(self):
        """Get all available voices from pyttsx3"""
        voices = self.pyttsx_engine.getProperty('voices')
        voice_list = []
        for idx, voice in enumerate(voices):
            voice_info = {
                'id': idx,
                'name': voice.name,
                'voice_id': voice.id,
                'languages': voice.languages,
                'gender': getattr(voice, 'gender', 'Unknown')
            }
            voice_list.append(voice_info)
        return voice_list
    
    def list_voices(self):
        """Display all available voices"""
        print("\n" + "="*60)
        print("AVAILABLE VOICES")
        print("="*60)
        
        # Show pyttsx3 voices
        print("\nSystem Voices (pyttsx3):")
        print("-" * 60)
        for voice in self.available_voices:
            gender_str = f"[{voice['gender']}]" if voice['gender'] != 'Unknown' else ""
            print(f"{voice['id']}: {voice['name']} {gender_str}")
        
        # Show gTTS accents (female-focused)
        print("\n\nGoogle TTS Accents (gTTS):")
        print("-" * 60)
        print("100: English - US (Female)")
        print("101: English - UK (Female)")
        print("102: English - Australia (Female)")
        print("103: English - India (Female)")
        print("104: English - South Africa (Female)")
        
        print("\n" + "="*60 + "\n")
    
    def text_to_speech_pyttsx3(self, text, voice_id=None, filename="output.wav"):
        """Convert text to speech using pyttsx3 with selected voice"""
        try:
            if voice_id is not None and 0 <= voice_id < len(self.available_voices):
                selected_voice = self.available_voices[voice_id]
                self.pyttsx_engine.setProperty('voice', selected_voice['voice_id'])
                print(f"Using voice: {selected_voice['name']}")
            
            # Adjust rate and volume for better quality
            self.pyttsx_engine.setProperty('rate', 150)  # Speed of speech
            self.pyttsx_engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
            
            output_path = self.output_dir / filename
            self.pyttsx_engine.save_to_file(text, str(output_path))
            self.pyttsx_engine.runAndWait()
            
            print(f"✓ Audio saved to: {output_path}")
            return str(output_path)
        except Exception as e:
            print(f"✗ Error with pyttsx3: {e}")
            return None
    
    def text_to_speech_gtts(self, text, lang='en', tld='com', filename="output.mp3"):
        """Convert text to speech using Google TTS"""
        try:
            output_path = self.output_dir / filename
            
            # Create gTTS object with accent
            tts = gTTS(text=text, lang=lang, tld=tld, slow=False)
            tts.save(str(output_path))
            
            print(f"✓ Audio saved to: {output_path}")
            return str(output_path)
        except Exception as e:
            print(f"✗ Error with gTTS: {e}")
            return None
    
    def convert_text(self, text, voice_choice):
        """Main conversion function that routes to appropriate TTS engine"""
        if voice_choice < 100:
            # Use pyttsx3 for system voices
            return self.text_to_speech_pyttsx3(text, voice_choice, f"voice_{voice_choice}.wav")
        else:
            # Use gTTS for Google voices
            tld_map = {
                100: 'com',      # US
                101: 'co.uk',    # UK
                102: 'com.au',   # Australia
                103: 'co.in',    # India
                104: 'co.za',    # South Africa
            }
            tld = tld_map.get(voice_choice, 'com')
            return self.text_to_speech_gtts(text, 'en', tld, f"voice_gtts_{voice_choice}.mp3")

def main():
    """Main application entry point"""
    app = VoiceApp()
    
    print("\n" + "="*60)
    print("VOICE CLONING & TEXT-TO-SPEECH APPLICATION")
    print("="*60)
    print("\nWelcome! This app allows you to convert text to speech")
    print("with various voice options.")
    
    while True:
        print("\nMain Menu:")
        print("1. List available voices")
        print("2. Convert text to speech")
        print("3. Quick convert (default female voice)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            app.list_voices()
        
        elif choice == '2':
            app.list_voices()
            voice_id = input("\nEnter voice ID: ").strip()
            try:
                voice_id = int(voice_id)
            except ValueError:
                print("✗ Invalid voice ID")
                continue
            
            text = input("\nEnter text to convert: ").strip()
            if not text:
                print("✗ Text cannot be empty")
                continue
            
            print("\nConverting...")
            app.convert_text(text, voice_id)
        
        elif choice == '3':
            text = input("\nEnter text to convert: ").strip()
            if not text:
                print("✗ Text cannot be empty")
                continue
            
            print("\nConverting with default female voice (Google US)...")
            app.text_to_speech_gtts(text, tld='com', filename="quick_output.mp3")
        
        elif choice == '4':
            print("\nThank you for using Voice Cloning App!")
            break
        
        else:
            print("✗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
