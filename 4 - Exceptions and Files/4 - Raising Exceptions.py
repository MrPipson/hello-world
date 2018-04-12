# You can raise exceptions by using the raise statement.

print(1)
raise ValueError
print(2)

# You need to specify the type of the exception raised.

# which errors occur in this code?

try:
    print(1 / 0)
except ZeroDivisionError:
    raise ValueError

# both Zero and Value errors occur eventhough the ZeroDivisionError is not logged in the output


# Exceptions can be raised with arguments that give detail about them.
# For example:

name = "123"
raise NameError("Invalid name")

# raise an error "Negative" if the input number is Negative

num = input("Input any number:")
if float(num) < 0:
    raise ValueError("Negative number")

# In except blocks, the raise statement can be used without arguments
# to re-raise whatever exception occurred.

try:
    num = 5 / 0
except:
    print("An error occurred")
    raise
    
