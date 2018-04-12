# To ensure some code runs no matter what errors occur, you can use a finally statement.
# The finally statement is placed at the bottom of a try/except statement.
# Code within a finally statement always runs after execution of the code in the try,
# and possibly in the except, blocks.

try:
    print("hello world")
    print(1/0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")

try:
    print(1)
except:
    print(2)
finally:
    print(3)

# this code will print 1 3

# Code in a finally statement even runs if an uncaught exception occurs in one of the preceding blocks.

try:
    print(1)
    print(1/0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("This is executed last and always")
