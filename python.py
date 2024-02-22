import pyttsx3
import docx

engine = pyttsx3.init()

def speak_text_from_file(file_path):
    doc = docx.Document(file_path)
    for paragraph in doc.paragraphs:
        text = paragraph.text
        if text.strip():
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[2].id)
            try:
                engine.say(text)
                engine.runAndWait()
            except RuntimeError as e:
                print(f"Error while speaking: {e}")

file_path = input("Enter the path to the Word file: ")
speak_text_from_file(file_path)

engine.stop()
