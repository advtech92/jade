import speech_recognition as sr
from voice import say
from intents import handle_intent

# Define the wake word
wake_word = "Jade"

# Define the speech recognition function
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        text = r.recognize_sphinx(audio)
        print(f"You said: {text}")
        if wake_word.lower() in text.lower():
            # Get the intent from the text
            intent = get_intent(text)
            response = handle_intent(intent)
            say(response)
    except sr.UnknownValueError:
        print("PocketSphinx could not understand audio")
    except sr.RequestError as e:
        print(f"PocketSphinx error; {e}")

# Define the function to get the intent from text
def get_intent(text):
    # TODO: implement intent recognition
    return "greeting"

# Call the speech recognition function
recognize_speech()
