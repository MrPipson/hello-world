# Lists are another type of object in Python. They are used to store an indexed list of items.
# A list is created using square brackets with commas separating items.
# The certain item in the list can be accessed by using its index in square brackets.

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

# The first list item's index is 0, rather than 1, as might be expected.

# An empty list is created with an empty pair of square brackets.

empty_list = []
print(empty_list)

# Most of the time, a comma won't follow the last item in a list.
# However, it is perfectly valid to place one there, and it is encouraged in some cases.

# Typically, a list will contain items of a single item type, but it is also
# possible to include several different types. Lists can also be nested within other lists.

number = 3
things = ["string", 0, [0, 1, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

# Lists of lists are often used to represent 2D grids, as Python lacks the
# multidimensional arrays that would be used for this in other languages.

# the first line of code assigns the variable 'number' to the value of '3'.
# Printing [2][2] prints the third list entry's (the nested list's) third entry -
# which is the variable 'number' which has been assigned the value '3'.

# Indexing out of the bounds of possible list values causes an IndexError.
# Some types, such as strings, can be indexed like lists. Indexing strings behaves
# as though you are indexing a list containing each character in the string.
# For other types, such as integers, indexing them isn't possible, and it causes a TypeError.

str = "Hello world"
print(str[6])
