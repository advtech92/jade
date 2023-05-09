def handle_intent(intent):
    if intent == "greeting":
        return "Hello, how can I assist you?"
    elif intent == "weather":
        return "The weather today is sunny."
    else:
        return "I'm sorry, I don't understand that command."