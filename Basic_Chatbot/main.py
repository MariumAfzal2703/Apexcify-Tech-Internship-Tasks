def chatbot():
    while True:   # chatbot tab tak chalega jab tak user 'bye' na likhe
        user_input = input("You: ")   # user se input lena

        if user_input.lower() == "hello":
            print("Bot: Hi!")
        elif user_input.lower() == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input.lower() == "bye":
            print("Bot: Goodbye!")
            break   # loop band karna (chatbot ruk jaye)
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()  