# This lesson is about an example Python project: a simple calculator.
# Each part explains a different section of the program.
# The first section is the overall menu. This keeps on accepting user input until
#  the user enters "quit", so a while loop is used.

#OVERALL MENU - user input until quit

while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'substract' to substract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to quit the program")

    user_input = input("Enter one of the above: ")
    if user_input == "quit":
        break
    elif user_input == "add":
        # - insert code for addition
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number to add: "))
        result = num1 + num2
        print("Your result is: ")
        print(result)
    elif user_input == "substract":
        # - insert code for subtraction
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number to substract: "))
        result = num1 - num2
        print("Your result is:" + str(result))
    elif user_input == "multiply":
        # - insert code for multiplication
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number to multiply: "))
        result = num1 * num2
        print("Your result is: ")
        print(result)
    elif user_input == "divide":
        # - insert code for division
        num1 = float(input("Enter the nominator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
        print("The result of division is: ")
        print(result)
    else:
        print("Unknown input")

# The code above is the starting point for our program. It accepts user input,
# and compares it to the options in the if/elif statements.
# The break statement is used to stop the while loop, in case the user inputs "quit".
