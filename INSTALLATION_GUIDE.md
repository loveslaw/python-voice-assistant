# Detailed Installation Guide

This guide will help you install and run the Python Voice Assistant.

## Prerequisites

- **Python 3.7 or higher** - [Download here](https://www.python.org/downloads/)
- **A working microphone** - Built-in or external
- **Internet connection** - Required for speech recognition and web features

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/loveslaw/python-voice-assistant.git
cd python-voice-assistant
```

### 2. Create a Virtual Environment (Recommended)

Creating a virtual environment keeps your project dependencies isolated.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Platform-Specific Setup

#### **Windows Setup**

1. Most packages should install without issues.
2. If you encounter issues with PyAudio:
   - Download the pre-built wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
   - Find the wheel matching your Python version (e.g., `PyAudio-0.2.13-cp39-cp39-win_amd64.whl` for Python 3.9)
   - Install it:
   ```bash
   pip install PyAudio-0.2.13-cp39-cp39-win_amd64.whl
   ```

3. For screenshot functionality, you may need Pillow:
   ```bash
   pip install pillow
   ```

#### **macOS Setup**

1. First, install Homebrew if you don't have it:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Install PortAudio (required for PyAudio):
   ```bash
   brew install portaudio
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. For better speech recognition, update your security settings to allow microphone access to Terminal.

#### **Linux Setup**

1. Install system dependencies (Ubuntu/Debian):
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip python3-dev portaudio19-dev libportaudio2
   ```

2. Install Python audio library:
   ```bash
   sudo apt-get install python3-pyaudio
   ```

   Or via pip:
   ```bash
   pip install pyaudio
   ```

3. Install other Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install additional tools for some features:
   ```bash
   sudo apt-get install gnome-screensaver  # For lock screen feature
   ```

## Verification

To verify everything is working:

1. **Test Python installation:**
   ```bash
   python --version
   ```

2. **Test microphone:**
   ```python
   python -c "import pyaudio; print('PyAudio OK')"
   ```

3. **Test speech recognition:**
   ```python
   python -c "import speech_recognition; print('SpeechRecognition OK')"
   ```

4. **Test text-to-speech:**
   ```python
   python -c "import pyttsx3; engine = pyttsx3.init(); engine.say('Test'); engine.runAndWait(); print('pyttsx3 OK')"
   ```

## Running the Assistant

Start the assistant with:

```bash
python voice_assistant.py
```

You should hear a greeting and see the message "Listening..." in your terminal.

## Troubleshooting

### Issue: "No module named 'pyaudio'"

**Windows:**
- Download pre-compiled wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- Install with: `pip install <filename>.whl`

**macOS:**
```bash
brew install portaudio
pip install --upgrade pyaudio
```

**Linux:**
```bash
sudo apt-get install python3-pyaudio
```

### Issue: Microphone not detected

1. Check if microphone is connected and enabled in system settings
2. Test with: `python -m speech_recognition`
3. Restart the application

### Issue: Speech recognition not working

1. Ensure internet connection is active
2. Check Google Speech API service is accessible
3. Speak clearly and distinctly
4. Reduce background noise

### Issue: Audio output not working

1. Check speakers/headphones are connected
2. Increase volume in system settings
3. Adjust speech volume in `voice_assistant.py`:
   ```python
   engine.setProperty('volume', 0.9)  # Increase this value
   ```

### Issue: Application crashes on startup

1. Try running in debug mode:
   ```bash
   python -u voice_assistant.py
   ```
2. Check for Python/library compatibility issues
3. Reinstall dependencies:
   ```bash
   pip install --upgrade --force-reinstall -r requirements.txt
   ```

## Optional: Additional Features Setup

### For Screenshot Feature
```bash
pip install pillow
```

### For Weather and System Info
```bash
pip install psutil requests
```

### For Better Documentation
```bash
pip install sphinx
```

## Next Steps

1. Read the [README.md](README.md) for a complete feature overview
2. Customize settings in [config.py](config.py)
3. Explore [advanced_features.py](advanced_features.py) for additional capabilities
4. Start using the assistant with voice commands!

## Getting Help

- Check the [README.md](README.md) for command examples
- Read inline code comments for technical details
- Visit the GitHub issues page to report bugs
- Refer to library documentation:
  - [pyttsx3](https://pyttsx3.readthedocs.io/)
  - [SpeechRecognition](https://github.com/Uberi/speech_recognition)
  - [Wikipedia-API](https://wikipedia.readthedocs.io/)

## Performance Tips

1. **Improve Microphone Recognition:**
   - Adjust `ENERGY_THRESHOLD` in `config.py`
   - Increase `AMBIENT_NOISE_DURATION` for noisier environments

2. **Improve Speech Output:**
   - Adjust `SPEECH_RATE` for faster/slower speaking
   - Adjust `SPEECH_VOLUME` for louder/quieter output

3. **Reduce Latency:**
   - Ensure good internet connection for speech recognition
   - Close other applications using audio
   - Use a quality microphone

Enjoy your voice assistant!
