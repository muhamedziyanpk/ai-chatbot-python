print("AI Chatbot: Hello! I am Ziyan Bot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How can I help you?")
        
    elif user == "your name":
        print("Bot: My name is Ziyan Bot.")
        
    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")
        
    elif user == "bye":
        print("Bot: Goodbye!")
        break
        
    else:
        print("Bot: Sorry, I don't understand.")
