
import eel
import os
import subprocess
import pyttsx3
import speech_recognition as sr

eel.init("web")

engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('voice', engine.getProperty('voices')[1].id)

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

software_map = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "photoshop": "C:\\Program Files\\Adobe\\Adobe Photoshop 2024\\Photoshop.exe",
}

@eel.expose
def handle_command(command):
    command = command.lower().strip()
    if "open" in command:
        for key in software_map:
            if key in command:
                path = software_map[key]
                try:
                    subprocess.Popen(path)
                    speak(f"Opening {key}")
                    return f"✅ Opening {key.capitalize()}..."
                except Exception as e:
                    return f"❌ Failed to open {key}: {e}"
        return "⚠️ Software not found in list."
    elif "close" in command:
        for key in software_map:
            if key in command:
                os.system(f"taskkill /f /im {os.path.basename(software_map[key])}")
                speak(f"Closing {key}")
                return f"🛑 Closed {key.capitalize()}."
        return "⚠️ Software not found to close."
    elif command in ["hi", "hello", "jarvis"]:
        speak("Hello Siddhant. I am online and ready.")
        return "Hello Siddhant. I am online and ready."
    speak(command)
    return f"You said: {command}"

@eel.expose
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        try:
            query = recognizer.recognize_google(audio)
            return handle_command(query)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return "❌ Could not understand you."
        except sr.RequestError:
            return "❌ Mic or speech service error."

eel.start("index.html", size=(800, 600), port=8088)
