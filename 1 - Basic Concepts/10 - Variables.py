'''
# A variable allows you to store a value by assigning it to a name,
# which can be used to refer to the value later in the program.

x = 7
print(x)

print(x + 3)

print(x) # keeps the first assigned value

# Variables can be reassigned as many times as you want, in order to change their value.
# In Python, variables don't have specific types, so you can assign a string to a variable,
# and later assign an integer to the same variable.

x = 123
print(x)

x = "This is a string"
print(x + "!")

# Variable Names
# Certain restrictions apply in regard to the characters that may be used in Python
# variable names. The only characters that are allowed are letters, numbers, and underscores.
# Also, they can't start with numbers.
# Not following these rules results in errors.

this_is_a_variable_name = 7
123abc = 7
'''
# Trying to reference a variable you haven't assigned to causes an error.
# You can use the del statement to remove a variable, which means the reference
# from the name to the value is deleted, and trying to use the variable causes an error.
# Deleted variables can be reassigned to later as normal.

foo = "a string"
print(foo)
#print(bar) - NameError: name bar is not defined
del foo
#print(foo) - NameError: name foo is not defined (the variable was deleted)
