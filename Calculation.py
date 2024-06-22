'''
Calculator Project Instructions:
Overview:
Create a Python program that functions as a basic calculator. It takes user input 
to perform mathematical operations, displays results, and provides additional 
functionalities like displaying instructions, history of operations, and clearing 
the terminal screen.

Requirements:
User Input:

Prompt the user to input mathematical expressions (e.g., '5 + 5', '3 * 4').
Operation Parsing:

Use the split(" + ") method to parse the entered expressions.
Terminal Clearing Functionality:

Include the functionality to clear the terminal screen using os.system("clear").
Infinite Loop:

Implement an infinite loop so that the program continuously operates until the user 
enters the "exit" command.
Command Handling:

If the user inputs "help", display instructions about the program's functionalities.
If the command is "history", create a file using the with keyword to store a 
structured history of operations. Each entry should include the date and time of 
the operation along with the entered expression.
Example Structure for Operation History:

Operation 1:
23 Jan, 15:29. Operation - "5 + 3 * 2"

Implement the mentioned functionalities using appropriate Python constructs, 
ensuring the program's reliability and user-friendliness. Additionally, consider 
security concerns, especially when evaluating user-entered expressions.
'''

import os
import datetime
import math

def clear_screen():
    os.system("clear")

def evaluate_expression(expression):
    try:
        if 'sqrt' in expression:
            result = eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt})
        else:
            result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def save_to_history(operation):
    with open("calculator_history.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%d %b, %H:%M")
        file.write(f"Operation: {timestamp}. Expression - \"{operation}\"\n")

def display_help():
    print("\n=== Calculator Help ===")
    print("Enter mathematical expressions (exam: '5 + 5', '3 * 4').")
    print("Type 'help' to display this message again.")
    print("Type 'history' to view operation history.")
    print("Type 'exit' to quit the program.")

def main():
    clear_screen()
    display_help()
    
    while True:
        expression = input("\nEnter expression: ")
        
        if expression.lower() == "exit":
            print("Exiting calculator...")
            break
        
        elif expression.lower() == "help":
            clear_screen()
            display_help()
        
        elif expression.lower() == "history":
            try:
                with open("calculator_history.txt", "r") as file:
                    print("\n=== Operation History ===")
                    print(file.read())
            except FileNotFoundError:
                print("No history available.")
        
        else:
            result = evaluate_expression(expression)
            print(f"Result: {result}")
            save_to_history(expression)

if __name__ == "__main__":
    if not os.path.exists("calculator_history.txt"):
        with open("calculator_history.txt", "w") as file:
            file.write("Calculator History:\n")
    main()