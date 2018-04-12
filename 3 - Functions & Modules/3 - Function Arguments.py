# Arguments
#
# All the function definitions we've looked at so far have been functions of zero
# arguments, which are called with empty parentheses.
# However, most functions take arguments.
# The example below defines a function that takes one argument:

def print_with_exclamation(word):
    print(word + "!")

print_with_exclamation("Spam") # output is Spam!
print_with_exclamation("Eggs")
print_with_exclamation("Python")

# As you can see, the argument is defined inside the parentheses.

# the argument (word) is an empty variable waiting to be filled with a value when
# you use the function and put something within the parentheses

# You can also define functions with more than one argument; separate them with commas.

def print_sum_twice(x, y):
    print(x + y)
    print(x + y)

print_sum_twice(3, 4)

# Function arguments can be used as variables inside the function definition.
# However, they cannot be referenced outside of the function's definition.
# This also applies to other variables created inside a function.

def function(variable):
    variable += 1
    print(variable)

function(8) # prints output 9
print(variable) # gives NameError sine variable is not defined outside the function

# Technically, parameters are the variables in a function definition, and arguments
# are the values put into parameters when functions are called.
