"""
Advanced Features Module for Voice Assistant
Contains additional features that can be integrated into the main assistant
"""

import pyttsx3
import subprocess
import platform
import os
from datetime import datetime
import json


def get_weather(city):
    """Get weather information for a city"""
    try:
        import requests
        api_key = "open-meteo"  # Using open-meteo free API (no key needed)
        
        # Geocode the city to get coordinates
        geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geo_response = requests.get(geocoding_url)
        geo_data = geo_response.json()
        
        if not geo_data.get('results'):
            return f"Could not find weather data for {city}"
        
        location = geo_data['results'][0]
        latitude = location['latitude']
        longitude = location['longitude']
        
        # Get weather data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weather_code&timezone=auto"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        
        current = weather_data['current']
        temp = current['temperature_2m']
        weather_code = current['weather_code']
        
        return f"The weather in {city} is {temp} degrees with code {weather_code}"
    
    except Exception as e:
        return f"Sorry, I couldn't get the weather. {str(e)}"


def get_system_info():
    """Get system information"""
    try:
        import psutil
        
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        
        info = f"CPU usage is at {cpu_percent} percent. Memory usage is at {memory_percent} percent."
        return info
    except ImportError:
        return "psutil library not installed. Install with: pip install psutil"


def set_reminder(reminder_text, minutes=5):
    """Set a reminder"""
    import time
    import threading
    
    def reminder_timer():
        time.sleep(minutes * 60)
        engine = pyttsx3.init()
        engine.say(f"Reminder: {reminder_text}")
        engine.runAndWait()
    
    thread = threading.Thread(target=reminder_timer, daemon=True)
    thread.start()
    
    return f"Reminder set for {minutes} minutes from now"


def read_file(file_path):
    """Read and speak contents of a text file"""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        engine = pyttsx3.init()
        engine.say(f"Reading {file_path}")
        engine.say(content)
        engine.runAndWait()
        return True
    except FileNotFoundError:
        return f"File {file_path} not found"
    except Exception as e:
        return f"Error reading file: {str(e)}"


def create_file(file_path, content):
    """Create a new file with content"""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return f"File {file_path} created successfully"
    except Exception as e:
        return f"Error creating file: {str(e)}"


def list_files(directory="."):
    """List all files in a directory"""
    try:
        files = os.listdir(directory)
        return files
    except Exception as e:
        return f"Error listing files: {str(e)}"


def get_battery_info():
    """Get battery information (requires psutil)"""
    try:
        import psutil
        battery = psutil.sensors_battery()
        
        if battery is None:
            return "No battery detected (might be a desktop)"
        
        percent = battery.percent
        plugged = battery.power_plugged
        status = "charging" if plugged else "not charging"
        
        return f"Battery is at {percent} percent and is {status}"
    except ImportError:
        return "psutil library not installed. Install with: pip install psutil"


def adjust_volume(level):
    """Adjust system volume"""
    level = max(0, min(100, int(level)))  # Clamp between 0-100
    
    try:
        if platform.system() == "Windows":
            # Using nircmd or similar tools
            os.system(f"nircmd.exe setsysvolume {level * 655}")
            return f"Volume set to {level} percent"
        elif platform.system() == "Darwin":  # macOS
            os.system(f"osascript -e 'set volume output volume {level}'")
            return f"Volume set to {level} percent"
        elif platform.system() == "Linux":
            os.system(f"amixer set Master {level}%")
            return f"Volume set to {level} percent"
    except Exception as e:
        return f"Error adjusting volume: {str(e)}"


def shutdown_computer(delay_seconds=0):
    """Shutdown the computer"""
    try:
        if platform.system() == "Windows":
            os.system(f"shutdown /s /t {delay_seconds}")
        elif platform.system() in ["Darwin", "Linux"]:
            if delay_seconds > 0:
                os.system(f"sleep {delay_seconds} && shutdown -h now")
            else:
                os.system("shutdown -h now")
        return f"Shutting down computer in {delay_seconds} seconds"
    except Exception as e:
        return f"Error shutting down: {str(e)}"


def lock_screen():
    """Lock the screen"""
    try:
        if platform.system() == "Windows":
            os.system("rundll32.exe user32.dll,LockWorkStation")
        elif platform.system() == "Darwin":  # macOS
            os.system("open /System/Library/CoreServices/Menu\\ Extras/User.menu/Contents/Resources/CGSession -w")
        elif platform.system() == "Linux":
            os.system("gnome-screensaver-command --lock")
        return "Screen locked"
    except Exception as e:
        return f"Error locking screen: {str(e)}"


def check_internet_connection():
    """Check if internet connection is available"""
    try:
        import socket
        socket.create_connection(("1.1.1.1", 53), timeout=3)
        return "Internet connection is available"
    except OSError:
        return "No internet connection detected"


def toggle_wifi(enable=True):
    """Toggle WiFi (platform dependent)"""
    try:
        if platform.system() == "Windows":
            state = "on" if enable else "off"
            os.system(f"netsh interface set interface name=\"WiFi\" admin={state}")
            return f"WiFi turned {state}"
        elif platform.system() == "Darwin":  # macOS
            state = "on" if enable else "off"
            os.system(f"networksetup -setairportpower en0 {state}")
            return f"WiFi turned {state}"
        else:
            return "WiFi control not supported on this platform"
    except Exception as e:
        return f"Error toggling WiFi: {str(e)}"


# Dictionary of advanced functions for easy access
ADVANCED_FEATURES = {
    "weather": get_weather,
    "system_info": get_system_info,
    "reminder": set_reminder,
    "read_file": read_file,
    "create_file": create_file,
    "list_files": list_files,
    "battery": get_battery_info,
    "volume": adjust_volume,
    "shutdown": shutdown_computer,
    "lock": lock_screen,
    "internet": check_internet_connection,
    "wifi": toggle_wifi,
}
