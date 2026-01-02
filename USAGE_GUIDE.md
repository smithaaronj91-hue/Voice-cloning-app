# Voice Cloning App - Usage Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Finding the Right Voice](#finding-the-right-voice)
3. [Using Text-to-Speech](#using-text-to-speech)
4. [Advanced Features](#advanced-features)
5. [Tips and Best Practices](#tips-and-best-practices)

## Getting Started

### Quick Start (3 Easy Steps)

1. **Install the app:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the web interface:**
   ```bash
   python web_app.py
   ```

3. **Open your browser:**
   Navigate to `http://localhost:5000`

That's it! You're ready to create voice content.

## Finding the Right Voice

### Recommended Female Voices

The app includes several high-quality female voices specifically designed to meet your needs:

#### **Top Recommendations:**

1. **English - US (Female)** [Voice ID: 100]
   - Best for: Clear, professional American accent
   - Tone: Warm, friendly, and natural
   - Use case: General purpose, professional content

2. **English - UK (Female)** [Voice ID: 101]
   - Best for: Elegant British accent
   - Tone: Sophisticated and clear
   - Use case: Formal content, educational material

3. **English - Australia (Female)** [Voice ID: 102]
   - Best for: Friendly Australian accent
   - Tone: Casual and approachable
   - Use case: Conversational content, casual narration

4. **English - India (Female)** [Voice ID: 103]
   - Best for: Indian English accent
   - Tone: Clear with cultural authenticity
   - Use case: Diverse content, multicultural projects

5. **English - South Africa (Female)** [Voice ID: 104]
   - Best for: South African accent
   - Tone: Unique and engaging
   - Use case: Distinctive voice character

### How to Test Voices

#### Method 1: Web Interface
1. Open the web app at `http://localhost:5000`
2. Select a voice from the dropdown menu
3. Enter sample text like: "Hello, this is a test of my voice."
4. Click "Convert to Speech"
5. Listen and compare different voices

#### Method 2: Command Line
```bash
python voice_app.py
```
Then:
- Choose option 1 to list voices
- Choose option 2 to test a specific voice
- Choose option 3 for quick test with default female voice

#### Method 3: Demo Script
```bash
python demo.py
```
This generates sample audio with multiple voices for comparison.

## Using Text-to-Speech

### Web Interface (Easiest)

1. **Select Your Voice:**
   - Browse the voice dropdown
   - Female voices are in the "Google TTS" section
   - Each voice shows gender and accent information

2. **Enter Your Text:**
   - Type or paste your text in the text area
   - Supports any length (longer texts work best with Google TTS)
   - Can include punctuation for natural pauses

3. **Convert:**
   - Click "Convert to Speech"
   - Wait a few seconds for processing
   - Audio player appears automatically

4. **Download:**
   - Click the download button to save the audio file
   - Files are saved as MP3 (Google TTS) or WAV (system voices)

### Command-Line Interface

```python
from voice_app import VoiceApp

app = VoiceApp()

# Using Google TTS for US female voice
text = "Hello, welcome to my voice cloning app!"
app.text_to_speech_gtts(text, tld='com', filename="my_audio.mp3")

# Using UK female voice
app.text_to_speech_gtts(text, tld='co.uk', filename="uk_voice.mp3")
```

### Python Script

Create a simple script:

```python
#!/usr/bin/env python3
from voice_app import VoiceApp

app = VoiceApp()

# Your text
my_text = """
Welcome to my audio content. 
This is an example of text-to-speech conversion 
with a beautiful female voice.
"""

# Generate audio with US female voice
app.text_to_speech_gtts(my_text, tld='com', filename="my_content.mp3")

print("✓ Audio generated successfully!")
print("File saved as: output/my_content.mp3")
```

Save this as `my_script.py` and run:
```bash
python my_script.py
```

## Advanced Features

### Voice Cloning with Coqui TTS

For more advanced voice customization:

```bash
python voice_cloner.py
```

Features:
- 100+ multi-speaker voices
- High-quality synthesis
- Professional voice quality
- More control over voice characteristics

### Batch Conversion

Create multiple audio files at once:

```python
from voice_app import VoiceApp

app = VoiceApp()

texts = [
    "Welcome to chapter one.",
    "Welcome to chapter two.",
    "Welcome to chapter three."
]

for i, text in enumerate(texts, 1):
    filename = f"chapter_{i}.mp3"
    app.text_to_speech_gtts(text, tld='com', filename=filename)
    print(f"Generated {filename}")
```

### Custom Voice Settings

Adjust speech rate and volume (pyttsx3 only):

```python
from voice_app import VoiceApp

app = VoiceApp()

# Adjust settings
app.pyttsx_engine.setProperty('rate', 150)    # Speed (default: 150)
app.pyttsx_engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

text = "This is spoken at a custom rate and volume."
app.text_to_speech_pyttsx3(text, filename="custom.wav")
```

## Tips and Best Practices

### For Best Voice Quality

1. **Use Google TTS for female voices:**
   - Highest quality and most natural
   - Better pronunciation and intonation
   - Recommended for the "nice black woman voice" requirement

2. **Write naturally:**
   - Use conversational language
   - Include punctuation for natural pauses
   - Break long sentences into shorter ones

3. **Test before bulk conversion:**
   - Try different voices with sample text
   - Listen to the full output
   - Adjust text formatting if needed

### Text Formatting Tips

```
Good: "Hello! How are you today? I'm doing great."
Better intonation and natural pauses

Avoid: "Hello how are you today I'm doing great"
Runs together without natural breaks
```

### File Organization

```
output/
├── content_us_female.mp3      # US voice content
├── content_uk_female.mp3      # UK voice content
├── narration_part1.mp3        # First part
├── narration_part2.mp3        # Second part
└── final_mix.mp3              # Combined audio
```

### Performance Optimization

1. **For many conversions:**
   - Use Google TTS (faster for multiple files)
   - Process in batches
   - Save frequently used voices

2. **For offline use:**
   - Use pyttsx3 system voices
   - Pre-generate common phrases
   - Cache audio files

### Troubleshooting Common Issues

**Issue:** Voice sounds robotic
- **Solution:** Use Google TTS instead of system voices
- **Solution:** Add more punctuation for natural pauses

**Issue:** Audio file not playing
- **Solution:** Check file format (MP3 vs WAV)
- **Solution:** Verify audio player supports the format

**Issue:** Conversion takes too long
- **Solution:** Shorten text segments
- **Solution:** Use system voices for faster processing

**Issue:** Can't find the right female voice
- **Solution:** Try all Google TTS options (ID 100-104)
- **Solution:** Use voice cloner for more options
- **Solution:** Adjust rate and pitch in post-processing

## Example Use Cases

### 1. Audiobook Narration
```python
from voice_app import VoiceApp

app = VoiceApp()

chapters = {
    "Chapter 1": "Once upon a time...",
    "Chapter 2": "The next day...",
    # ... more chapters
}

for title, content in chapters.items():
    filename = f"{title.lower().replace(' ', '_')}.mp3"
    app.text_to_speech_gtts(content, tld='com', filename=filename)
```

### 2. Podcast Intro
```python
intro = """
Welcome to our podcast! 
I'm your host, and today we'll be discussing 
amazing topics that you'll love.
"""

app.text_to_speech_gtts(intro, tld='com', filename="podcast_intro.mp3")
```

### 3. Educational Content
```python
lesson = """
Today's lesson is about text-to-speech technology.
This powerful tool can help make content accessible
to everyone, regardless of their reading abilities.
"""

app.text_to_speech_gtts(lesson, tld='co.uk', filename="lesson_01.mp3")
```

### 4. Automated Announcements
```python
announcement = """
Attention please. 
The store will be closing in 15 minutes.
Thank you for shopping with us today.
"""

app.text_to_speech_gtts(announcement, tld='com', filename="closing_announcement.mp3")
```

## Getting Help

- **Questions?** Check the main README.md
- **Issues?** Open an issue on GitHub
- **Feature requests?** Submit a pull request or issue

---

**Happy voice creating!** 🎤✨
