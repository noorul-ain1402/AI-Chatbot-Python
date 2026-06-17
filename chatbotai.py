print("=" * 60)
print("🤖 SMART RULE-BASED AI CHATBOT")
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.")
print("=" * 60)

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hi there! How can I help you today?")

    elif user in ["your name", "what is your name"]:
        print("Bot: My name is DecodeBot.")

    elif user == "who created you":
        print("Bot: I was created using Python programming.")

    elif user == "how are you":
        print("Bot: I'm doing great! What about you?")

    elif user in ["i am fine", "fine", "good"]:
        print("Bot: Glad to hear that! 😊")

    elif user == "not good":
        print("Bot: I hope things get better soon.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "python":
        print("Bot: Python is a popular programming language.")

    elif user == "cloud":
        print("Bot: Cloud computing delivers services over the internet.")

    elif user == "cybersecurity":
        print("Bot: Cybersecurity protects systems from attacks.")


    elif user == "joke":
        print("Bot: Why do programmers prefer dark mode?")
        print("Bot: Because light attracts bugs! 😂")

    elif user == "fact":
        print("Bot: The first computer bug was an actual moth.")

    elif user == "motivate me":
        print("Bot: Small progress every day leads to big success.")

    elif user == "2+2":
        print("Bot: 4")

    elif user == "5*5":
        print("Bot: 25")

    elif user == "good morning":
        print("Bot: Good morning! Have a productive day.")

    elif user == "good afternoon":
        print("Bot: Good afternoon!")

    elif user == "good night":
        print("Bot: Good night. Sleep well!")


    elif user == "help":
        print("\nAvailable Commands:")
        print("hello, hi, hey")
        print("how are you")
        print("your name")
        print("who created you")
        print("ai")
        print("python")
        print("cloud")
        print("cybersecurity")
        print("joke")
        print("fact")
        print("motivate me")
        print("good morning")
        print("good afternoon")
        print("good night")
        print("bye")

    elif user == "bye":
        print("Bot: Goodbye! Have a wonderful day. 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see commands.")