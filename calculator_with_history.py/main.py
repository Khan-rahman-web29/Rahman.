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
 