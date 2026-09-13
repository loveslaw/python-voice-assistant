# Python Voice Assistant (JARVIS-like)

A simple yet powerful desktop voice assistant built in Python that listens to voice commands and performs various tasks on your computer.

## Features

### Voice Interaction
- **Speech Recognition**: Listens to your voice commands using Google's Speech Recognition API
- **Text-to-Speech**: Responds to you with natural-sounding speech using pyttsx3

### Basic Commands
- **Greeting**: Get a friendly greeting based on time of day
- **Time**: Ask for the current time
- **Date**: Ask for today's date

### Web Tasks
- **Website Access**: Open popular websites (Google, YouTube, GitHub, Twitter, Facebook, Reddit, StackOverflow, Wikipedia, Amazon, LinkedIn)
- **Google Search**: Search for anything on Google
- **Wikipedia Lookup**: Search for a person/topic on Wikipedia and get a summary

### Desktop Control
- **Launch Applications**: Open any installed application
- **Music Player**: Open your default music player
- **Screenshots**: Take screenshots and automatically save them with timestamps
- **Quick Notes**: Save quick text notes to a file with timestamps

### Entertainment
- **Jokes**: Get random programming jokes to lighten your day

### Help
- **Help Command**: Get a list of all available commands

## Installation

### Prerequisites
- Python 3.7 or higher
- A microphone connected to your computer

### Setup

1. Clone the repository:
```bash
git clone https://github.com/loveslaw/python-voice-assistant.git
cd python-voice-assistant
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. For Windows users, you might need to install additional audio libraries:
```bash
pip install pyaudio
```

   **If you have issues with PyAudio on Windows:**
   - Download the wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
   - Install it with: `pip install PyAudio‑0.2.13‑cp39‑cp39‑win_amd64.whl` (adjust the filename for your Python version)

4. For Linux users:
```bash
sudo apt-get install python3-pyaudio
```

5. For macOS users:
```bash
brew install portaudio
pip install pyaudio
```

## Usage

Start the voice assistant:
```bash
python voice_assistant.py
```

The assistant will greet you and start listening for commands. Simply speak naturally!

## Available Commands

| Command | Example | Description |
|---------|---------|-------------|
| Greeting | "Hello" or "Hi" | Get a greeting |
| Time | "What time is it?" | Get the current time |
| Date | "What's today's date?" | Get today's date |
| Open Website | "Open Google" or "Open YouTube" | Open a website |
| Search | "Search Python tutorials" | Search on Google |
| Wikipedia | "Wikipedia Albert Einstein" | Search Wikipedia and get info |
| Launch App | "Launch Notepad" or "Open app Chrome" | Launch an application |
| Music | "Play music" | Open your music player |
| Screenshot | "Take a screenshot" | Capture and save screenshot |
| Save Note | "Note remember to buy milk" | Save a quick note |
| Joke | "Tell me a joke" | Get a random joke |
| Help | "Help" | See all available commands |
| Exit | "Exit" or "Bye" | Exit the assistant |

## Supported Websites

The assistant has quick access to these popular websites:
- Google
- YouTube
- GitHub
- Twitter
- Facebook
- Reddit
- StackOverflow
- Wikipedia
- Amazon
- LinkedIn

You can also ask it to open any other website by URL.

## Files

- `voice_assistant.py` - Main application file
- `requirements.txt` - Python dependencies
- `voice_notes.txt` - Auto-generated file where quick notes are saved
- `screenshot_*.png` - Screenshots are saved with timestamps

## Project Structure

```
python-voice-assistant/
├── voice_assistant.py      # Main application
├── requirements.txt        # Dependencies
├── README.md              # This file
├── voice_notes.txt        # Generated notes file
└── screenshot_*.png       # Generated screenshots
```

## Troubleshooting

### "No module named 'pyaudio'"
- On Windows: Download and install PyAudio wheel file manually
- On Linux: `sudo apt-get install python3-pyaudio`
- On macOS: `brew install portaudio` then `pip install pyaudio`

### "Sorry, I didn't understand that"
- Speak clearly and distinctly
- Reduce background noise
- Check your microphone is working

### "Could not connect to speech recognition service"
- Ensure you have an active internet connection (Google Speech Recognition requires it)
- Check your internet connectivity

### Speech not working
- Ensure your speakers/audio output is working
- Check volume level in the code (adjust `engine.setProperty('volume', 0.9)`)

## Future Enhancements

- Offline speech recognition
- Custom voice commands configuration
- Integration with smart home devices
- Weather forecast
- Email sending
- Calendar integration
- Task reminders
- News updates
- System information display

## Requirements

- Python 3.7+
- pyttsx3 - Text-to-speech
- SpeechRecognition - Voice recognition
- PyAudio - Audio I/O
- requests - HTTP library (for future enhancements)
- wikipedia - Wikipedia API
- PIL/Pillow - Image processing for screenshots

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork, modify, and improve this project! Pull requests are welcome.

## Disclaimer

This is a personal project created for educational purposes. It's a simplified version inspired by JARVIS. Use responsibly and ensure you have proper permissions before automating tasks on your system.
