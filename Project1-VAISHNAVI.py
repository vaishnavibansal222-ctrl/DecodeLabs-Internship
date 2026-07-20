import time
import random
import datetime

# ==========================================
# Rule-Based AI Chatbot
# Developed by: Vaishnavi Bansal
# DecodeLabs Internship Project
# ==========================================

knowledge_base = {
    "what is ai":
        "Artificial Intelligence enables computers to perform tasks that normally require human intelligence.",

    "what is python":
        "Python is a simple, powerful, and beginner-friendly programming language.",

    "who are you":
        "I am SmartBot, a Rule-Based AI Chatbot.",

    "what is your name":
        "My name is SmartBot.",

    "who created you":
        "I was developed by Vaishnavi Bansal for the DecodeLabs Internship.",

    "what can you do":
        "I can answer basic questions, tell the date, time, share quotes, jokes, and perform simple calculations.",

    "thank you":
        "You're welcome! Happy to help."
}

quotes = [
    "Success is the result of consistent effort.",
    "Learning never stops.",
    "Believe in yourself and keep improving."
]

jokes = [
    "Why do Python programmers wear glasses? Because they can't C!",
    "Debugging is like being a detective in your own mystery novel.",
    "Why was the computer cold? It forgot to close its Windows!"
]

greetings = ["hi", "hello", "hey"]

exit_commands = ["exit", "bye", "quit"]

print("=" * 60)
print("             SMARTBOT")
print("       Rule-Based AI Chatbot")
print("     Developed by Vaishnavi Bansal")
print("=" * 60)

print("\nType 'help' to see available commands.")
print("Type 'exit' to close the chatbot.\n")

while True:

    user = input("You : ").lower().strip()

    if user in exit_commands:
        print("\nSmartBot : Thank you for chatting. Goodbye!")
        break

    elif user in greetings:
        print("SmartBot : Hello! How can I assist you today?")

    elif user == "help":
        print("\nAvailable Commands")
        print("----------------------------")
        print("hello / hi")
        print("what is ai")
        print("what is python")
        print("who are you")
        print("who created you")
        print("what can you do")
        print("time")
        print("date")
        print("quote")
        print("joke")
        print("calculator")
        print("thank you")
        print("exit")
        print("----------------------------")

    elif user == "time":
        print("SmartBot :", datetime.datetime.now().strftime("%I:%M:%S %p"))

    elif user == "date":
        print("SmartBot :", datetime.date.today())

    elif user == "quote":
        print("SmartBot :", random.choice(quotes))

    elif user == "joke":
        print("SmartBot :", random.choice(jokes))

    elif user == "calculator":
        try:
            num1 = float(input("Enter first number : "))
            operator = input("Enter (+, -, *, /) : ")
            num2 = float(input("Enter second number : "))

            if operator == "+":
                print("Result =", num1 + num2)
            elif operator == "-":
                print("Result =", num1 - num2)
            elif operator == "*":
                print("Result =", num1 * num2)
            elif operator == "/":
                if num2 != 0:
                    print("Result =", num1 / num2)
                else:
                    print("Cannot divide by zero.")
            else:
                print("Invalid operator.")
        except:
            print("Invalid input.")

    elif user in knowledge_base:
        print("SmartBot :", knowledge_base[user])

    else:
        print("SmartBot : Sorry, I don't understand that.")
        print("Type 'help' to view the available commands.")

print("\nProgram Ended Successfully.")
