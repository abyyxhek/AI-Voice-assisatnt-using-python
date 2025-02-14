import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)  # Use Google Speech Recognition
        print("You said: " + text)
        return text.lower()  # Convert to lowercase for easier handling
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def respond(text):
    if "hello" in text:
        print("Hello there!")
    elif "what's the weather" in text:
        print("I'm not connected to a weather service yet, but I can tell you it's a beautiful day!")  # Placeholder
    elif "set an alarm" in text:
        print("I can't set alarms yet, but that's a great feature to add!") # Placeholder
    elif "jarvis" in text:
        print("Yes, I am here.")


    elif "exit" in text or "quit" in text:
        print("Goodbye!")
        exit()
    else:
        print("I didn't understand that.  Try saying 'hello', 'what's the weather', 'set an alarm', or 'jarvis'.")

if __name__ == "__main__":
    while True:
        user_input = listen()
        if user_input:
            respond(user_input)