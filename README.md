# Voice Cloning & Text-to-Speech Application 🎤

A powerful and easy-to-use voice cloning and text-to-speech application with multiple voice options, including beautiful female voices from various accents. **Perfect for finding a nice, warm female voice and converting text to speech once you've found the right one!**

## 🌟 Perfect For Your Needs

This app is specifically designed to help you:
1. **Find the right female voice** - Test multiple high-quality female voices
2. **Convert text to speech** - Easy conversion once you've found your preferred voice
3. **Create professional audio** - Generate natural-sounding voice content

### Recommended Female Voices

**Voice 100: US Female (⭐ BEST CHOICE)**
- Clear, warm American accent
- Professional and natural-sounding
- Perfect for most content types

**Voice 101: UK Female**
- Elegant British accent
- Sophisticated tone

**Voice 102: Australian Female**
- Friendly, casual accent
- Approachable and warm

**Voice 103: Indian Female**
- Clear Indian English
- Cultural authenticity

**Voice 104: South African Female**
- Unique South African accent
- Distinctive character

## Features ✨

- **Multiple Voice Options**: Choose from various female voices including US, UK, Australian, Indian, and South African accents
- **Two TTS Engines**: 
  - Google Text-to-Speech (gTTS) for high-quality online voices
  - pyttsx3 for offline system voices
- **Advanced Voice Cloning**: Optional Coqui TTS integration for sophisticated voice cloning
- **Web Interface**: Beautiful, modern web UI for easy text-to-speech conversion
- **Command-Line Interface**: Full-featured CLI for power users
- **Audio Export**: Download generated audio files in WAV or MP3 format

## Installation 🚀

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/smithaaronj91-hue/Voice-cloning-app.git
cd Voice-cloning-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Note: For full voice cloning features, TTS library may require additional system dependencies. On Linux:
```bash
sudo apt-get install espeak-ng
```

## Usage 📖

### Web Interface (Recommended)

Start the web server:
```bash
python web_app.py
```

Then open your browser and navigate to: `http://localhost:5000`

The web interface provides:
- Easy voice selection with voice type indicators
- Text input area for your content
- Real-time audio preview
- Download functionality for generated audio

### Command-Line Interface

Run the main application:
```bash
python voice_app.py
```

Follow the interactive menu to:
1. List available voices
2. Convert text to speech with your chosen voice
3. Quick convert with default female voice
4. Exit the application

### Advanced Voice Cloning

For advanced voice cloning features using Coqui TTS:
```bash
python voice_cloner.py
```

This provides:
- Multi-speaker TTS with 100+ voices
- High-quality voice synthesis
- Voice cloning from reference audio (experimental)

## Quick Start Example 🎯

### Using Python
```python
from voice_app import VoiceApp

app = VoiceApp()

# List all available voices
app.list_voices()

# Convert text with Google TTS (US female voice)
app.text_to_speech_gtts("Hello! Welcome to the voice cloning app.", tld='com')

# Convert text with a system voice
app.text_to_speech_pyttsx3("This is a test.", voice_id=0)
```

## Voice Options 🎵

### Google TTS Voices (Recommended for Female Voices)
- **English - US (Female)**: Clear, neutral American accent
- **English - UK (Female)**: Elegant British accent
- **English - Australia (Female)**: Friendly Australian accent
- **English - India (Female)**: Indian English accent
- **English - South Africa (Female)**: South African accent

### System Voices
Your system's built-in TTS voices (varies by operating system)

### Coqui TTS (Advanced)
100+ multi-speaker voices with high-quality synthesis

## Output Files 📁

Generated audio files are saved in the `output/` directory:
- Google TTS generates `.mp3` files
- System TTS generates `.wav` files
- Coqui TTS generates `.wav` files

## Tips for Best Results 💡

1. **For Natural Female Voices**: Use Google TTS options (voice ID 100-104)
2. **For Offline Use**: Use pyttsx3 system voices
3. **For Voice Customization**: Try the advanced voice cloner with different speakers
4. **For Longer Texts**: Google TTS handles long texts better
5. **Audio Quality**: Coqui TTS provides the highest quality but requires more resources

## Troubleshooting 🔧

### "No module named 'TTS'"
The advanced voice cloning features are optional. The basic app works without it. To enable:
```bash
pip install TTS
```

### "espeak not found"
Install espeak for pyttsx3:
- **Linux**: `sudo apt-get install espeak-ng`
- **macOS**: `brew install espeak`
- **Windows**: Usually works out of the box

### Web interface not loading
Make sure port 5000 is not in use:
```bash
# Check if port is in use
netstat -an | grep 5000

# Use a different port
python web_app.py --port 8000
```

## Project Structure 📂

```
Voice-cloning-app/
├── voice_app.py           # Main CLI application
├── voice_cloner.py        # Advanced voice cloning module
├── web_app.py             # Web interface
├── templates/
│   └── index.html         # Web UI template
├── output/                # Generated audio files
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Contributing 🤝

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License 📄

This project is open source and available for personal and commercial use.

## Acknowledgments 🙏

- [gTTS](https://github.com/pndurette/gTTS) - Google Text-to-Speech
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3) - Text-to-Speech library
- [Coqui TTS](https://github.com/coqui-ai/TTS) - Advanced TTS and voice cloning
- [Flask](https://flask.palletsprojects.com/) - Web framework

## Support 💬

For questions or issues, please open an issue on GitHub.

---

**Enjoy creating amazing voice content!** 🎉
