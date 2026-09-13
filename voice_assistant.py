import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import subprocess
import os
import json
import platform
import time
import random
from pathlib import Path

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level

# Initialize speech recognition
recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000

# Notes file path
NOTES_FILE = "voice_notes.txt"

# Jokes database
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the developer go broke? Because he used up all his cache!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why do Java developers wear glasses? Because they don't C#!",
    "What's a programmer's favorite hangout place? Foo Bar!",
    "Why did the Python developer go to the beach? To get some byte!",
]


def speak(text):
    """Convert text to speech"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen for voice input and convert to text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Please try again.")
            return ""
        except sr.RequestError:
            speak("Sorry, I couldn't connect to the speech recognition service.")
            return ""
        except sr.Timeout:
            speak("I didn't hear anything. Please try again.")
            return ""


def greet_user():
    """Greet the user based on time of day"""
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good morning! I'm your voice assistant. How can I help you?"
    elif hour < 18:
        greeting = "Good afternoon! I'm your voice assistant. What can I do for you?"
    else:
        greeting = "Good evening! I'm your voice assistant. How can I assist you?"
    
    speak(greeting)


def get_time():
    """Tell the current time"""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")


def get_date():
    """Tell the current date"""
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"Today is {current_date}")


def open_website(website_name):
    """Open a website in the default browser"""
    websites = {
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
    
    url = websites.get(website_name.lower())
    if url:
        speak(f"Opening {website_name}")
        webbrowser.open(url)
    else:
        speak(f"I don't have {website_name} in my favorites. Opening it with the URL.")
        webbrowser.open(f"https://{website_name}.com")


def google_search(query):
    """Search on Google"""
    speak(f"Searching for {query}")
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)


def wikipedia_search(person):
    """Search Wikipedia and read summary"""
    try:
        import wikipedia
        speak(f"Searching Wikipedia for {person}")
        summary = wikipedia.summary(person, sentences=3)
        speak(summary)
    except ImportError:
        speak("Wikipedia library is not installed. Please install it with pip install wikipedia")
    except wikipedia.exceptions.DisambiguationError:
        speak(f"There are multiple results for {person}. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak(f"I couldn't find {person} on Wikipedia.")


def launch_application(app_name):
    """Launch an application"""
    app_name = app_name.lower()
    
    try:
        if platform.system() == "Windows":
            os.startfile(app_name)
            speak(f"Launching {app_name}")
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", app_name])
            speak(f"Launching {app_name}")
        elif platform.system() == "Linux":
            subprocess.Popen([app_name])
            speak(f"Launching {app_name}")
    except Exception as e:
        speak(f"I couldn't launch {app_name}. It might not be installed.")


def play_music():
    """Open music player"""
    speak("Opening music player")
    system = platform.system()
    
    try:
        if system == "Windows":
            os.startfile("wmplayer.exe")
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", "Music"])
        elif system == "Linux":
            subprocess.Popen(["rhythmbox"])
    except:
        speak("Couldn't open music player. Please open it manually.")


def take_screenshot():
    """Take a screenshot and save it"""
    try:
        from PIL import ImageGrab
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        screenshot = ImageGrab.grab()
        screenshot.save(filename)
        speak(f"Screenshot saved as {filename}")
    except ImportError:
        speak("PIL library is not installed. Install it with pip install pillow")
    except Exception as e:
        speak(f"Error taking screenshot: {str(e)}")


def take_note(note_text):
    """Save a quick note to a text file"""
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(NOTES_FILE, "a") as file:
            file.write(f"[{timestamp}] {note_text}\n")
        speak(f"Note saved: {note_text}")
    except Exception as e:
        speak(f"Error saving note: {str(e)}")


def tell_joke():
    """Tell a random joke"""
    joke = random.choice(JOKES)
    speak(joke)


def show_help():
    """Show available commands"""
    help_text = """
    Available Commands:
    - "hello" or "hi": Get a greeting
    - "time": Get current time
    - "date": Get current date
    - "open [website]": Open a website (google, youtube, github, etc.)
    - "search [query]": Search on Google
    - "wikipedia [person]": Search and read about someone on Wikipedia
    - "launch [app]": Launch an application
    - "music": Open music player
    - "screenshot": Take a screenshot
    - "note [text]": Save a quick note
    - "joke": Tell me a joke
    - "help": Show this help message
    - "exit": Exit the assistant
    """
    print(help_text)
    speak("I can help you with many tasks. Here are some commands you can use: hello, time, date, open a website, search Google, look up Wikipedia, launch apps, play music, take a screenshot, save notes, tell jokes, and more!")


def process_command(command):
    """Process voice commands"""
    command = command.strip()
    
    if not command:
        return True
    
    # Greeting commands
    if "hello" in command or "hi" in command:
        speak("Hello! How can I assist you?")
    
    # Time and date commands
    elif "time" in command:
        get_time()
    
    elif "date" in command:
        get_date()
    
    # Website commands
    elif "open" in command:
        website = command.replace("open", "").strip()
        if website:
            open_website(website)
        else:
            speak("Which website would you like to open?")
    
    # Google search
    elif "search" in command or "google" in command:
        query = command.replace("search", "").replace("google", "").strip()
        if query:
            google_search(query)
        else:
            speak("What would you like me to search for?")
    
    # Wikipedia search
    elif "wikipedia" in command:
        person = command.replace("wikipedia", "").strip()
        if person:
            wikipedia_search(person)
        else:
            speak("Who would you like me to search for on Wikipedia?")
    
    # Launch application
    elif "launch" in command or "open app" in command:
        app_name = command.replace("launch", "").replace("open app", "").strip()
        if app_name:
            launch_application(app_name)
        else:
            speak("Which application would you like to launch?")
    
    # Music
    elif "music" in command or "play music" in command:
        play_music()
    
    # Screenshot
    elif "screenshot" in command:
        take_screenshot()
    
    # Take note
    elif "note" in command:
        note_text = command.replace("note", "").strip()
        if note_text:
            take_note(note_text)
        else:
            speak("What note would you like me to save?")
    
    # Joke
    elif "joke" in command:
        tell_joke()
    
    # Help
    elif "help" in command:
        show_help()
    
    # Exit
    elif "exit" in command or "quit" in command or "bye" in command:
        speak("Goodbye! Have a great day!")
        return False
    
    else:
        speak("I didn't understand that command. Say 'help' to see available commands.")
    
    return True


def main():
    """Main function to run the voice assistant"""
    print("=" * 50)
    print("Welcome to Python Voice Assistant")
    print("=" * 50)
    
    greet_user()
    
    print("\nSay 'help' to see available commands or start giving me commands!")
    print("Say 'exit' to quit the assistant.\n")
    
    while True:
        command = listen()
        if command:
            should_continue = process_command(command)
            if not should_continue:
                break
        time.sleep(1)


if __name__ == "__main__":
    main()
