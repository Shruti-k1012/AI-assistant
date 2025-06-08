import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import time
# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# Function to make the assistant speak
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the service.")
        return ""

# Function to process commands
def respond(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {current_time}")
    
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    elif 'search' in command:
        search_query = command.replace('search', '').strip()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            speak(f"Searching Google for {search_query}")
            webbrowser.open(url)
        else:
            speak("Please say what you want to search for.")
    
    elif 'exit' in command or 'quit' in command or 'bye' in command:
        speak("Goodbye! Have a great day.")
