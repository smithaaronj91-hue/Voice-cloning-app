#!/usr/bin/env python3
"""
Complete Example: Using the Voice Cloning App for Text-to-Speech
This example specifically demonstrates finding and using a nice female voice
as requested in the requirements.
"""

from voice_app import VoiceApp
from pathlib import Path

def example_1_quick_conversion():
    """Example 1: Quick text-to-speech conversion with default female voice"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Quick Conversion with Default Female Voice")
    print("="*70)
    
    app = VoiceApp()
    
    text = """
    Hello! Welcome to my voice cloning application. 
    I'm demonstrating text-to-speech conversion with a beautiful female voice.
    This is perfect for creating audio content, audiobooks, or any voice-over work.
    """
    
    print("\n📝 Converting text to speech...")
    print(f"Text: {text.strip()[:100]}...")
    
    # Using US female voice (recommended for warm, professional tone)
    app.text_to_speech_gtts(text, tld='com', filename='example1_quick.mp3')
    
    print("\n✅ Done! Audio saved to: output/example1_quick.mp3")
    print("-"*70)

def example_2_compare_voices():
    """Example 2: Compare different female voice accents"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Compare Different Female Voice Accents")
    print("="*70)
    
    app = VoiceApp()
    
    text = "Welcome! I'm here to help you create amazing voice content."
    
    voices = [
        {'name': 'US Female', 'tld': 'com', 'file': 'example2_us.mp3'},
        {'name': 'UK Female', 'tld': 'co.uk', 'file': 'example2_uk.mp3'},
        {'name': 'Australian Female', 'tld': 'com.au', 'file': 'example2_au.mp3'},
    ]
    
    print("\n📝 Generating samples for comparison...")
    
    for voice in voices:
        print(f"\n  → {voice['name']}... ", end='', flush=True)
        app.text_to_speech_gtts(text, tld=voice['tld'], filename=voice['file'])
        print("✓")
    
    print("\n✅ Generated 3 voice samples in output/ directory")
    print("   Listen to each one and pick your favorite!")
    print("-"*70)

def example_3_long_content():
    """Example 3: Convert longer content (like a paragraph or story)"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Converting Longer Content")
    print("="*70)
    
    app = VoiceApp()
    
    long_text = """
    Once upon a time, in a world of technology and innovation,
    there was a voice cloning application that could transform text into beautiful speech.
    This application was designed to help creators, educators, and storytellers
    bring their words to life with natural-sounding voices.
    
    The application featured multiple voice options, allowing users to choose
    the perfect voice for their content. Whether it was a warm American accent,
    an elegant British tone, or a friendly Australian sound, the choices were vast.
    
    And so, the voice cloning app became an essential tool for anyone
    who wanted to create engaging audio content. The end.
    """
    
    print("\n📝 Converting longer content...")
    print(f"Text length: {len(long_text)} characters")
    
    # US female voice works great for storytelling
    app.text_to_speech_gtts(long_text, tld='com', filename='example3_story.mp3')
    
    print("\n✅ Story converted! Audio saved to: output/example3_story.mp3")
    print("-"*70)

def example_4_custom_messages():
    """Example 4: Create multiple custom voice messages"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Creating Multiple Custom Voice Messages")
    print("="*70)
    
    app = VoiceApp()
    
    messages = {
        'greeting': "Hello! Thank you for calling. How can I help you today?",
        'on_hold': "Please hold while we connect you to the next available representative.",
        'thank_you': "Thank you for your patience. We appreciate your business.",
        'goodbye': "Thank you for calling. Have a wonderful day!"
    }
    
    print("\n📝 Creating custom voice messages...")
    
    for name, text in messages.items():
        filename = f'example4_{name}.mp3'
        print(f"\n  → {name.replace('_', ' ').title()}... ", end='', flush=True)
        app.text_to_speech_gtts(text, tld='com', filename=filename)
        print("✓")
    
    print("\n✅ Created 4 custom messages in output/ directory")
    print("-"*70)

def example_5_using_voice_id():
    """Example 5: Using voice IDs directly (useful for automation)"""
    print("\n" + "="*70)
    print("EXAMPLE 5: Using Voice IDs for Automation")
    print("="*70)
    
    app = VoiceApp()
    
    text = "This is an automated voice message generated using voice ID selection."
    
    # Voice IDs: 100=US, 101=UK, 102=AU, 103=IN, 104=ZA
    voice_id = 100  # US Female (recommended)
    
    print(f"\n📝 Converting with Voice ID {voice_id}...")
    app.convert_text(text, voice_id)
    
    print("\n✅ Conversion complete using voice ID!")
    print("   This method is great for batch processing and automation")
    print("-"*70)

def main():
    """Run all examples"""
    print("\n" + "="*70)
    print("VOICE CLONING APP - COMPLETE EXAMPLES")
    print("="*70)
    print("\nThese examples demonstrate how to use the voice cloning app")
    print("to convert text to speech with beautiful female voices.")
    print("\nNote: Internet connection required for Google TTS voices.")
    print("="*70)
    
    try:
        # Run each example
        example_1_quick_conversion()
        example_2_compare_voices()
        example_3_long_content()
        example_4_custom_messages()
        example_5_using_voice_id()
        
        print("\n" + "="*70)
        print("✅ ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("="*70)
        print("\n📁 Check the 'output/' directory for all generated audio files")
        print("\n💡 TIP: Listen to the different voice samples and choose")
        print("   the one that sounds best for your specific needs.")
        print("\n🎯 RECOMMENDED: US Female Voice (voice ID 100)")
        print("   - Warm, professional tone")
        print("   - Clear pronunciation")
        print("   - Perfect for most content types")
        print("\n" + "="*70 + "\n")
        
    except Exception as e:
        print(f"\n\n⚠️  ERROR: {e}")
        print("\nNote: Make sure you have:")
        print("  1. Installed dependencies: pip install -r requirements.txt")
        print("  2. Active internet connection (for Google TTS)")
        print("\nIf you're in an offline environment, use pyttsx3 system voices instead.")
        print("See USAGE_GUIDE.md for more information.")

if __name__ == "__main__":
    main()
