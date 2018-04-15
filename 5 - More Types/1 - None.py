# The None object is used to represent the absence of a value.
# It is similar to null in other programming languages.
# Like other "empty" values, such as 0, [] and the empty string, it is False when
# converted to a Boolean variable.
# When entered at the Python console, it is displayed as the empty string.

print("\n\n Excercise #1 - None \n")

None == None
print(None)

# The None object is returned by any function that doesn't
# explicitly return anything else.

print("\n\n Excercise #2 - None returned by a function that returns nothing\n")

def some_func():
    print("Hi!")

var = some_func()
print(var)


print("\n\n Now let's call a function that does return something")

def some_func2():
    print("Hi!")
    return("Something")

var2 = some_func2()
print(var2)
