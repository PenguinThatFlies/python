import pyttsx3

engine = pyttsx3.init()

def speak_text():
    while True:
        text = input("Enter text to speak (or 'q' to quit): ")

        if text.lower() == 'q':
            break

        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 50)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        try:
            engine.say(text)
            engine.runAndWait()
        except RuntimeError as e:
            print(f"Error while speaking: {e}")

speak_text()

engine.stop()
