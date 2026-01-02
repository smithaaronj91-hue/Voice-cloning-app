#!/usr/bin/env python3
"""
Test Google TTS functionality (the main feature for female voices)
"""

from gtts import gTTS
from pathlib import Path
import os

def test_gtts():
    """Test that gTTS works correctly"""
    print("\n" + "="*60)
    print("TESTING GOOGLE TTS (Main Feature)")
    print("="*60 + "\n")
    
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    test_text = "Hello! This is a test of the voice cloning app."
    
    # Test US female voice
    print("Testing US Female Voice...")
    try:
        tts = gTTS(text=test_text, lang='en', tld='com', slow=False)
        output_file = output_dir / "test_us_female.mp3"
        tts.save(str(output_file))
        
        if output_file.exists():
            file_size = output_file.stat().st_size
            print(f"✓ Successfully generated US female voice")
            print(f"  File: {output_file}")
            print(f"  Size: {file_size} bytes")
        else:
            print("✗ File not created")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    # Test UK female voice
    print("\nTesting UK Female Voice...")
    try:
        tts = gTTS(text=test_text, lang='en', tld='co.uk', slow=False)
        output_file = output_dir / "test_uk_female.mp3"
        tts.save(str(output_file))
        
        if output_file.exists():
            file_size = output_file.stat().st_size
            print(f"✓ Successfully generated UK female voice")
            print(f"  File: {output_file}")
            print(f"  Size: {file_size} bytes")
        else:
            print("✗ File not created")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    # Test Australian female voice
    print("\nTesting Australian Female Voice...")
    try:
        tts = gTTS(text=test_text, lang='en', tld='com.au', slow=False)
        output_file = output_dir / "test_au_female.mp3"
        tts.save(str(output_file))
        
        if output_file.exists():
            file_size = output_file.stat().st_size
            print(f"✓ Successfully generated Australian female voice")
            print(f"  File: {output_file}")
            print(f"  Size: {file_size} bytes")
        else:
            print("✗ File not created")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    print("\n" + "="*60)
    print("✅ ALL GTTS TESTS PASSED!")
    print("="*60)
    print("\n📁 Generated test files in output/ directory:")
    print("  - test_us_female.mp3")
    print("  - test_uk_female.mp3")
    print("  - test_au_female.mp3")
    print("\n✓ Core functionality verified!")
    print("✓ Female voice generation working correctly!")
    print("\n" + "="*60 + "\n")
    
    return True

if __name__ == "__main__":
    import sys
    success = test_gtts()
    sys.exit(0 if success else 1)
