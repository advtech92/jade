import speech_recognition as sr
from voice import say
from intents import handle_intent

# Define the wake word
wake_word = "Jade"

# Define the speech recognition function
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Say something!")
            audio = r.listen(source)
            try:
                text = r.recognize_sphinx(audio)
                print(f"You said: {text}")
                if wake_word.lower() in text.lower():
                    # Listen for a specific command
                    say("What can I do for you?")
                    command_audio = r.listen(source)
                    command_text = r.recognize_sphinx(command_audio)
                    print(f"You said: {command_text}")
                    # Check if user wants to exit during command
                    if "stop" in command_text.lower() or "exit" in command_text.lower():
                        say("Goodbye!")
                        break
                    # Get the intent from the command text
                    intent = get_intent(command_text)
                    response = handle_intent(intent)
                    say(response)
                    # Check if user wants to exit after command
                    if "stop" in response.lower() or "exit" in response.lower():
                        say("Goodbye!")
                        break
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