#!/usr/bin/env python3
"""
Web Interface for Voice Cloning App
Provides a simple web UI for text-to-speech conversion
"""

from flask import Flask, render_template, request, jsonify, send_file
import os
from pathlib import Path
from voice_app import VoiceApp
import json

app = Flask(__name__)
voice_app = VoiceApp()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/voices')
def get_voices():
    """API endpoint to get available voices"""
    voices = []
    
    # System voices
    for voice in voice_app.available_voices:
        voices.append({
            'id': voice['id'],
            'name': voice['name'],
            'type': 'system',
            'gender': voice.get('gender', 'Unknown')
        })
    
    # Google TTS voices
    google_voices = [
        {'id': 100, 'name': 'English - US (Female)', 'type': 'google', 'gender': 'Female'},
        {'id': 101, 'name': 'English - UK (Female)', 'type': 'google', 'gender': 'Female'},
        {'id': 102, 'name': 'English - Australia (Female)', 'type': 'google', 'gender': 'Female'},
        {'id': 103, 'name': 'English - India (Female)', 'type': 'google', 'gender': 'Female'},
        {'id': 104, 'name': 'English - South Africa (Female)', 'type': 'google', 'gender': 'Female'},
    ]
    voices.extend(google_voices)
    
    return jsonify(voices)

@app.route('/api/convert', methods=['POST'])
def convert_text():
    """API endpoint to convert text to speech"""
    try:
        data = request.json
        text = data.get('text', '')
        voice_id = int(data.get('voice_id', 100))
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        # Convert text to speech
        output_path = voice_app.convert_text(text, voice_id)
        
        if output_path:
            filename = os.path.basename(output_path)
            return jsonify({
                'success': True,
                'filename': filename,
                'path': output_path
            })
        else:
            return jsonify({'error': 'Conversion failed'}), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download/<filename>')
def download_audio(filename):
    """Download generated audio file"""
    try:
        # Validate filename to prevent directory traversal attacks
        # Only allow alphanumeric, underscores, hyphens, and dots
        import re
        if not re.match(r'^[\w\-\.]+$', filename):
            return jsonify({'error': 'Invalid filename'}), 400
        
        # Ensure the file is within the output directory
        file_path = voice_app.output_dir / filename
        
        # Check if the resolved path is actually within output_dir
        try:
            file_path = file_path.resolve()
            output_dir_resolved = voice_app.output_dir.resolve()
            if not str(file_path).startswith(str(output_dir_resolved)):
                return jsonify({'error': 'Access denied'}), 403
        except (OSError, RuntimeError):
            return jsonify({'error': 'Invalid file path'}), 400
        
        if file_path.exists():
            return send_file(file_path, as_attachment=True)
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("VOICE CLONING WEB APP")
    print("="*60)
    print("\nStarting web server...")
    print("Open your browser and navigate to: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server")
    print("\n⚠️  NOTE: This is running in DEBUG mode for development.")
    print("    For production use, set debug=False and use a production server.")
    print("="*60 + "\n")
    
    # Use host='127.0.0.1' for better security (only accessible locally)
    # Change to '0.0.0.0' only if you need network access
    app.run(debug=True, host='127.0.0.1', port=5000)
