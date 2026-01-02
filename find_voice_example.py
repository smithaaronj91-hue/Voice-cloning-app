#!/usr/bin/env python3
"""
Example: Finding and Using the Right Female Voice
Specifically for finding a "nice black woman voice" as requested
"""

from voice_app import VoiceApp
import os

def main():
    """Demonstrate finding and using the right female voice"""
    app = VoiceApp()
    
    print("\n" + "="*70)
    print("FINDING THE RIGHT FEMALE VOICE - EXAMPLE")
    print("="*70)
    print("\nThis example will help you find the perfect female voice")
    print("and demonstrate text-to-speech conversion.")
    print("-"*70)
    
    # Sample text that sounds natural with female voice
    sample_texts = [
        "Hello, I'm here to help you find the perfect voice for your content.",
        "Welcome! Let me introduce myself and show you what I can do.",
        "Good morning! I hope you're having a wonderful day.",
    ]
    
    # Test multiple female voices
    voice_configs = [
        {
            'name': 'US Female Voice',
            'description': 'Clear American accent - warm and professional',
            'tld': 'com',
            'filename': 'female_voice_us.mp3'
        },
        {
            'name': 'UK Female Voice',
            'description': 'British accent - elegant and sophisticated',
            'tld': 'co.uk',
            'filename': 'female_voice_uk.mp3'
        },
        {
            'name': 'Australian Female Voice',
            'description': 'Australian accent - friendly and casual',
            'tld': 'com.au',
            'filename': 'female_voice_au.mp3'
        },
        {
            'name': 'Indian Female Voice',
            'description': 'Indian English - clear with cultural authenticity',
            'tld': 'co.in',
            'filename': 'female_voice_in.mp3'
        },
    ]
    
    print("\n🎤 Generating sample voices for comparison...\n")
    
    for i, config in enumerate(voice_configs, 1):
        print(f"\n{i}. {config['name']}")
        print(f"   Description: {config['description']}")
        print(f"   Generating sample... ", end='', flush=True)
        
        # Use first sample text for consistency
        result = app.text_to_speech_gtts(
            sample_texts[0],
            tld=config['tld'],
            filename=config['filename']
        )
        
        if result:
            print("✓")
        else:
            print("✗ Failed")
    
    print("\n" + "="*70)
    print("✅ VOICE SAMPLES GENERATED!")
    print("="*70)
    
    print("\n📁 All samples are saved in the 'output/' directory:")
    for config in voice_configs:
        filepath = os.path.join('output', config['filename'])
        if os.path.exists(filepath):
            print(f"   ✓ {config['filename']}")
    
    print("\n" + "-"*70)
    print("\n📝 NEXT STEPS:")
    print("\n1. Listen to each sample voice file")
    print("2. Choose the voice that sounds best for your needs")
    print("3. Note the voice name (e.g., 'US Female Voice')")
    print("4. Use that voice for your text-to-speech conversions")
    
    print("\n" + "-"*70)
    print("\n💡 RECOMMENDATION:")
    print("\nFor a nice, warm female voice, we recommend:")
    print("   • US Female Voice (voice_gtts_100.mp3)")
    print("   • Professional, clear, and pleasant")
    print("   • Works well for most content types")
    
    print("\n" + "-"*70)
    print("\n🎯 USING YOUR CHOSEN VOICE:")
    print("\nOnce you've found the right voice, use it like this:")
    print("""
    from voice_app import VoiceApp
    
    app = VoiceApp()
    my_text = "Your content here"
    
    # For US female voice:
    app.text_to_speech_gtts(my_text, tld='com', filename='my_audio.mp3')
    
    # For UK female voice:
    app.text_to_speech_gtts(my_text, tld='co.uk', filename='my_audio.mp3')
    """)
    
    print("\n" + "-"*70)
    print("\n🌐 WEB INTERFACE:")
    print("\nFor easier voice selection, use the web interface:")
    print("   python web_app.py")
    print("   Then open: http://localhost:5000")
    
    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    main()
