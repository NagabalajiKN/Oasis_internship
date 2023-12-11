import speech_recognition as sr
import datetime
import pyttsx3
import wikipedia
import webbrowser
import time
import sys
import ctypes
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the properties for the speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)

engine.setProperty('pitch', 1.8)
console = Console()

def pulsating_ellipsis():
    cycles = 2  # Adjust the number of pulsation cycles as needed
    for _ in range(cycles):
        for i in range(4):
            sys.stdout.write(f"\033[K\rRecognizing 🔗 {'.' * i}   ")
            sys.stdout.flush()
            time.sleep(0.1)
        time.sleep(0.15)
    print("\n")

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now 🎙️", end='', flush=True)
        try:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=2)  # Set the timeout value (in seconds)
        except sr.WaitTimeoutError:
            print("     Timeout: No speech detected.\n")
            return None

    try:
        print("Thinking", end='', flush=True)
        pulsating_ellipsis()
        command = r.recognize_google(audio)
        command = command.lower()

        user_text = f'YOU: {command}\n'
        user_panel = Panel(Text(user_text, style= "bold green", justify="right"), width=93)
        console.print(user_panel)
        
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.\n")
        return None
    except sr.RequestError as e:
        print(f"Error fetching results; {e}")
        return None



def process_command(command):
    query = command.lower()
    
    if "your name" in command:
        speak("My name is Jarvis.")
    
    elif "hello" in command:
        speak("Hello sir! What can I do for you?")
    
    elif "how are you" in command:
        speak("I'm doing well,  thank you!")
    
    elif "good morning" in command:
        speak("Good Morning Sir!")
    
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"It's currently {current_time}")
    
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A %B %d, %Y")
        speak(f"Today's date is {current_date}")
    
    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    
    elif "search" in command:
        search_term = command.split("search", 1)[1].strip()
        google_search(search_term)
    
    elif 'open youtube' in command:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
    
    elif 'lock window' in command:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()
    
    elif 'help' in command:
        speak("The commands I can respond to are listed below.")
        print("+------------------------------------------------------------------------------------------+")
        print("Here are the list of commands you can use:")
        print("1. What is your name?")
        print("2. Hello")
        print("3. How are you?")
        print("4. Good Morning")
        print("5. What time is it?")
        print("6. What is today's date?")
        print("7. Search Wikipedia for [query]")
        print("8. Search Google for [query]")
        print("9. Open YouTube")
        print("10. Lock Window")
        print("11. Exit")
        print("+------------------------------------------------------------------------------------------+")
    elif "exit" in command or "bye" in command:
        speak("Goodbye for now, but I'll be back whenever you need me.")
        exit()
    else:
        speak("I'm not sure how to respond to that.")


def speak(text):
    jarvis_text = f'🤖JARVIS🤖: {text}\n'
    
    jarvis_panel = Panel(Text(jarvis_text, style="bold blue", justify="left"), width=93)
    console.print(jarvis_panel)

    engine.say(text)
    engine.runAndWait()


def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

print("                     ░░░░░██╗ ░█████╗ ░██████╗ ░██╗░░░██╗ ██╗ ░██████╗")
print("                     ░░░░░██║ ██╔══██╗ ██╔══██╗ ██║░░░██║ ██║ ██╔════╝")
print("                     ░░░░░██║ ███████║ ██████╔╝ ╚██╗░██╔╝ ██║ ╚█████╗░")
print("                     ██╗░░██║ ██╔══██║ ██╔══██╗ ░╚████╔╝░ ██║ ░╚═══██╗")
print("                     ╚█████╔╝ ██║░░██║ ██║░░██║ ░░╚██╔╝░░ ██║ ██████╔╝")
print("                     ░╚════╝ ░╚═╝░░╚═╝ ╚═╝░░╚═╝ ░░░╚═╝░░░ ╚═╝ ╚═════╝░")
print("+------------------------------------------------------------------------------------------+")
print("Starting Jarvis🚀...")
time.sleep(1)
print("Jarvis is ready to assist you!")
print("+------------------------------------------------------------------------------------------+")

# Continuous listening loop
while True:
    command = recognize_speech()
    if command:
        process_command(command)