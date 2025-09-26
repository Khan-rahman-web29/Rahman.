<<<<<<< HEAD
# 1 import the randm module 
# 2 create the subjects

import random
import random

# Funny and diverse subjects
subjects = [
    "Rahman Khan", 
    "Arshan Khan",
    "Mumbai Cat",
    "Arif Ansari",
    "Kaimganj Dogs",
    "Nirmala Sitaraman",
    "Narendra Modi",
    "Alien from Mars",
    "AI Robot GPT-5000",
    "A Flying Rickshaw",
    "Invisible Man",
    "Baba ka Dhaba Owner",
    "Kaimganj's Donkey"
]

# Wild & funny actions
actions = [
    "launches",
    "eats",
    "dances with",
    "declares war on",
    "celebrates",
    "is celebrating",
    "is sad about",
    "steals",
    "paints",
    "hacks",
    "buys",
    "sings to",
    "slaps"
]

# Weird & random things
things = [
    "a red fort",
    "the Taj Mahal",
    "public transport",
    "a plate of samosa",
    "something inside parliament",
    "the Ram Mandir",
    "Jatwara",
    "a flying cow",
    "a packet of Kurkure",
    "modi ji's chappal",
    "Arshan's tiffin box",
    "a spaceship full of pani puri",
    "a very angry parrot",
    "a haunted dosa"
]

# Start the headline generation loop 
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    thing = random.choice(things)

    headline = f"BREAKING NEWS: {subject} {action} {thing}!"
    print("\n" + headline)

    user = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user == "no":
        break

# Goodbye message
print("\nThanks for using Fake News Headline Generator. Have a hilarious day! 😄")

    









 
=======
history_file = "history.txt"

def show_history():
    try:
        with open(history_file, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No history found")
            else:
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found yet.")

def clear_history():
    with open(history_file, 'w') as file:
        pass
    print("History cleared...")

def save_history(equation, result):
    with open(history_file, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use format: number operator number (e.g. 8 + 3)")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])  
    except ValueError:
        print("Invalid numbers.")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("You cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use only + - * /")
        return

    if result == int(result):
        result = int(result)
    print("Result:", result)
    save_history(user_input, result)

def main():
    print('--- Simple Calculator ---')
    print('Type math operation (e.g. 5 + 3) or command: history, clear, exit')
    while True:
        user_input = input("Enter: ").strip().lower()
        if user_input == "exit":
            print("GOODBYE")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()
 
>>>>>>> 20a3ab17d8ebe3b545db1c8377c4a129494bd797
