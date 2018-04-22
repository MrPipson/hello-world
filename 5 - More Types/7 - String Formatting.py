# So far, to combine strings and non-strings, you've converted the non-strings to
# strings and added them. String formatting provides a more powerful way to embed
# non-strings within strings. String formatting uses a string's format method to
# substitute a number of arguments in the string.
# Example:

nums = [4, 5, 6]
msg = "Numbers: {0},{1}{2}".format(nums[0], nums[1], nums[2])
print(msg)

# Each argument of the format function is placed in the string at the corresponding
# position, which is determined using the curly braces { }.

# so numbers inside curly brackets{} are simply indexes of elements inside .format() bracket.
#
# msg = "Numbers: {0} {1} {3}". format(4,8,3,6)
# print(msg)
#
# >> Numbers: 4 8 6

# String formatting can also be done with named arguments.
# Example:

a = "{x}, {y}".format(x=5, y=12)
print(a)

# a = "{0}, {1}, {x}, {y}".format(1, 3, x=5, y=12)
# print(a)
# >>>1, 3, 5, 12
# but:
# a = "{0}, {1}, {x}, {y}, {2}".format(1, 3, x=5, y=12,15)
# print(a)
# >>> SyntaxError
