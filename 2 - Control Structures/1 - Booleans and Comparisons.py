
# Another type in Python is the Boolean type. There are two Boolean values: True and False.
# They can be created by comparing values, for instance by using the equal operator ==.

my_boolean = True
print(my_boolean)

x = 2 == 3
print(x)

y = "Hello" == "hello"
print(y)

y = 7 == 7.0
print(x)

# Another comparison operator, the not equal operator (!=), evaluates to True if
# the items being compared aren't equal, and False if they are.

x = "eleven" != "seven"
print(x)

y = 2 != 10
print(y)

# Python also has operators that determine whether one number (float or integer)
# is greater than or smaller than another. These operators are > and < respectively.

x = 7 < 5
print(x)

# The greater than or equal to, and smaller than or equal to operators are >= and <=.
# They are the same as the strict greater than and smaller than operators, except
# that they return True when comparing equal numbers.

x = 7 >= 8
print(x)

x = 7 >= 7
print(x)
