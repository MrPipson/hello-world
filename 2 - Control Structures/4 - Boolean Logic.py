# Boolean logic is used to make more complicated conditions for if statements that rely
# on more than one condition. Python's Boolean operators are and, or, and not. The and operator
# takes two arguments, and evaluates as True if, and only if, both of its arguments are True.
# Otherwise, it evaluates to False.

m = 1 == 1 and 2 == 2
print(m)

x = 1 == 1 and 2 != 2
print(x)

# The or operator also takes two arguments. It evaluates to True if either (or both)
# of its arguments are True, and False if both arguments are False.

x = 1 == 1 or 2 != 2
print(x)

# Unlike other operators we've seen so far, not only takes one argument, and inverts it.
# The result of not True is False, and not False goes to True.

x = not 1 == 1 
print(x)
