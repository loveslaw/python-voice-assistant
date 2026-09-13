"""
Configuration file for the Voice Assistant
Customize settings here without modifying the main application
"""

# Speech Recognition Settings
RECOGNITION_TIMEOUT = 5  # Seconds to wait for speech input
AMBIENT_NOISE_DURATION = 1  # Seconds to listen for noise calibration
ENERGY_THRESHOLD = 4000  # Microphone sensitivity threshold

# Text-to-Speech Settings
SPEECH_RATE = 150  # Words per minute
SPEECH_VOLUME = 0.9  # Volume level (0.0 to 1.0)

# Application Settings
NOTES_FILE = "voice_notes.txt"  # File to store quick notes
SCREENSHOTS_FOLDER = "screenshots"  # Folder to save screenshots

# Favorite Websites
FAVORITE_WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://www.github.com",
    "twitter": "https://www.twitter.com",
    "facebook": "https://www.facebook.com",
    "reddit": "https://www.reddit.com",
    "stackoverflow": "https://www.stackoverflow.com",
    "wikipedia": "https://www.wikipedia.com",
    "amazon": "https://www.amazon.com",
    "linkedin": "https://www.linkedin.com",
}

# Joke Database
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the developer go broke? Because he used up all his cache!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why do Java developers wear glasses? Because they don't C#!",
    "What's a programmer's favorite hangout place? Foo Bar!",
    "Why did the Python developer go to the beach? To get some byte!",
    "How do you comfort a JavaScript bug? You console it!",
    "Why did the developer go to the beach? To get some HTML!",
    "Why do C developers never get lonely? Because they're always using pointers to everyone!",
    "What's a programmer's favorite place to hang out? The Foo Bar!",
]

# Default Applications (customize for your system)
DEFAULT_APPLICATIONS = {
    "notepad": "notepad",
    "calculator": "calc",
    "browser": "chrome",
    "editor": "notepad++",
    "terminal": "cmd",
    "music": "wmplayer",
}

# Speech Recognition API Settings
USE_GOOGLE_SPEECH_API = True  # Use Google's free API
GOOGLE_API_KEY = None  # Not needed for basic usage

# Logging Settings
ENABLE_LOGGING = True
LOG_FILE = "assistant_log.txt"

# Debug Mode
DEBUG_MODE = False  # Set to True for verbose output
