import datetime
import random

def chatbot():
    print("Chatbot: Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        # Greetings
        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello there! How can I help you today?")

        # Name query
        elif "your name" in user_input:
            print("Chatbot: I am RuleBot, your assistant chatbot.")

        # How are you
        elif "how are you" in user_input:
            print("Chatbot: I'm functioning perfectly. Thanks for asking!")

        # Help
        elif "help" in user_input:
            print("Chatbot: I can tell jokes, do basic math, show time/date, and more!")

        # Time
        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {now}")

        # Date
        elif "date" in user_input:
            today = datetime.datetime.now().strftime("%A, %d %B %Y")
            print(f"Chatbot: Today is {today}")

        # Joke
        elif "joke" in user_input:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the computer go to therapy? It had too many bytes of trauma.",
                "Parallel lines have so much in common… it’s a shame they’ll never meet."
            ]
            print(f"Chatbot: {random.choice(jokes)}")

        # Weather placeholder
        elif "weather" in user_input:
            print("Chatbot: I can't fetch live weather yet, but it's always sunny in here!")

        # Basic calculator
        elif "calculate" in user_input:
            try:
                expression = user_input.replace("calculate", "").strip()
                result = eval(expression)
                print(f"Chatbot: The result is {result}")
            except:
                print("Chatbot: Sorry, I couldn't calculate that. Try expressions like 'calculate 5 + 3'.")

        # Mood detection
        elif "i am sad" in user_input or "i feel sad" in user_input:
            print("Chatbot: I'm sorry to hear that. Remember, it's okay to feel down. You're not alone! 🌟")

        elif "i am happy" in user_input:
            print("Chatbot: That’s wonderful to hear! 😊 Keep smiling!")

        # Exit
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Unknown input
        else:
            print("Chatbot: I'm not sure how to respond to that.")
            with open("unknown_inputs.txt", "a") as f:
                f.write(user_input + "\n")

# Run the chatbot
chatbot()
