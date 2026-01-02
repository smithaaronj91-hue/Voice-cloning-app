# Quick Start Guide

## Installation

### Step 1: Install Python
Make sure you have Python 3.8 or higher installed:
```bash
python3 --version
```

### Step 2: Clone the Repository
```bash
git clone https://github.com/smithaaronj91-hue/Voice-cloning-app.git
cd Voice-cloning-app
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Note for Linux users:** You may need espeak for pyttsx3:
```bash
sudo apt-get install espeak-ng
```

## Quick Start (3 Ways to Use)

### Method 1: Web Interface (Easiest) ⭐

**Perfect for finding and testing different voices!**

1. Start the web server:
```bash
python web_app.py
```

2. Open your browser to: `http://localhost:5000`

3. Select a female voice from the dropdown (voice ID 100-104)

4. Enter your text and click "Convert to Speech"

5. Listen and download your audio!

### Method 2: Find Voice Example Script

**Specifically designed to help find the right female voice:**

```bash
python find_voice_example.py
```

This will:
- Generate sample audio with different female voices
- Save them all to the `output/` folder
- Let you compare and choose your favorite

### Method 3: Command Line Interactive

```bash
python voice_app.py
```

Then follow the menu:
1. List available voices
2. Convert text to speech (choose voice ID)
3. Quick convert with default female voice
4. Exit

## Your First Conversion

### Option A: Quick Python Script

Create a file called `my_first_voice.py`:

```python
from voice_app import VoiceApp

app = VoiceApp()

# Your text
text = "Hello! Welcome to the voice cloning app. This is my first text to speech conversion!"

# Convert with US female voice (recommended)
app.text_to_speech_gtts(text, tld='com', filename='my_first_audio.mp3')

print("✓ Done! Check output/my_first_audio.mp3")
```

Run it:
```bash
python my_first_voice.py
```

### Option B: Quick Command Line

For the fastest test:
```bash
python -c "from voice_app import VoiceApp; VoiceApp().text_to_speech_gtts('Hello world', filename='test.mp3')"
```

Check `output/test.mp3`!

## Recommended Female Voices

Based on your requirement for "a nice black woman voice", here are the best options:

### Voice 100: US Female (⭐ RECOMMENDED)
- **Description**: Clear, warm American accent
- **Best for**: Professional content, narration, general purpose
- **Code**: `tld='com'` or voice ID `100`

### Voice 101: UK Female
- **Description**: Elegant British accent
- **Best for**: Formal content, sophisticated tone
- **Code**: `tld='co.uk'` or voice ID `101`

### Voice 102: Australian Female
- **Description**: Friendly, casual accent
- **Best for**: Conversational content, approachable tone
- **Code**: `tld='com.au'` or voice ID `102`

### Voice 103: Indian Female
- **Description**: Clear with cultural authenticity
- **Best for**: Diverse content, multicultural projects
- **Code**: `tld='co.in'` or voice ID `103`

## Next Steps

1. **Test Multiple Voices**: Run `python find_voice_example.py` to generate samples
2. **Choose Your Favorite**: Listen to all the samples
3. **Start Creating**: Use your chosen voice for your content!
4. **Explore Advanced Features**: Try `python voice_cloner.py` for 100+ voices

## Common Use Cases

### Audiobook Narration
```python
from voice_app import VoiceApp

app = VoiceApp()
chapters = ["Chapter 1 text...", "Chapter 2 text...", ...]

for i, chapter in enumerate(chapters, 1):
    app.text_to_speech_gtts(chapter, tld='com', filename=f'chapter_{i}.mp3')
```

### Podcast Intro
```python
intro = "Welcome to my podcast! Today we're discussing..."
app.text_to_speech_gtts(intro, tld='com', filename='podcast_intro.mp3')
```

### Quick Announcements
```python
announcement = "The store will close in 15 minutes. Thank you!"
app.text_to_speech_gtts(announcement, tld='com', filename='announcement.mp3')
```

## Troubleshooting

### Import Errors
```bash
# Make sure dependencies are installed
pip install -r requirements.txt
```

### No Internet Connection
- Google TTS (voice 100-104) requires internet
- Use system voices (pyttsx3) for offline

### espeak Error
- This only affects pyttsx3 (system voices)
- Google TTS voices work without espeak
- On Linux: `sudo apt-get install espeak-ng`

### Web Interface Won't Start
```bash
# Check if port 5000 is in use
netstat -an | grep 5000

# Kill any process using it, or use different port in web_app.py
```

## Tips for Best Results

1. **For Natural Sound**: Use Google TTS (voices 100-104)
2. **For Long Text**: Break into smaller paragraphs
3. **For Pauses**: Use punctuation (periods, commas, etc.)
4. **For Emphasis**: Try UPPERCASE for important words
5. **For Speed**: Adjust rate parameter in advanced settings

## Getting Help

- **Full Documentation**: See `README.md`
- **Detailed Usage**: See `USAGE_GUIDE.md`
- **Issues**: Open an issue on GitHub
- **Examples**: Check `demo.py` and `find_voice_example.py`

---

**Ready to create amazing voice content!** 🎤✨
