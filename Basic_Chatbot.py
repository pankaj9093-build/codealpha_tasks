def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi there!"
    elif user_input == "hi":
        return "Hello!"
    elif user_input == "how are you":
        return "I'm doing great, thanks! How about you?"
    elif user_input == "i'm fine" or user_input == "i am fine":
        return "Glad to hear that!"
    elif user_input == "what's your name" or user_input == "what is your name":
        return "I'm just a simple chatbot. You can call me ChatBuddy."
    elif user_input == "will you be my friend.":
        return "yess!"
    elif user_input == " will you be my girlfriend" or user_input == "will you be my gf":
        return "no sorry i am loyal for my boyfriend."
    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that yet."

print("Welcome to ChatBuddy! Type something to chat. Type 'bye' to exit.\n")

while True:
    user_message = input("You: ")

    reply = chatbot_response(user_message)
    print("ChatBuddy:", reply)

    if user_message.lower().strip() == "bye" or user_message.lower().strip() == "goodbye":
        break

print("\n Chat ended.")

