import speech_recognition as sr
import pyttsx3
import pyautogui
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-US')
        print(f"User said: {command}\n")
    except Exception as e:
        print("Could not understand, please say that again.")
        return None

    return command.lower()

def execute_command(command):
    if 'open notepad' in command:
        speak('Opening Notepad')
        os.system('notepad.exe')

    elif 'close notepad' in command:
        speak('Closing Notepad')
        os.system('taskkill /f /im notepad.exe')

    elif 'screenshot' in command:
        speak('Taking a screenshot')
        pyautogui.screenshot('screenshot.png')
        speak('Screenshot taken')

    # Add more commands as needed

if __name__ == "__main__":
    while True:
        command = take_command()
        if command:
            execute_command(command)
        if 'stop listening' in command:
            speak("Stopping voice assistant")
            break
