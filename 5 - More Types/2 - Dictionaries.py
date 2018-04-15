# Dictionaries are data structures used to map arbitrary keys to values.
# Lists can be thought of as dictionaries with integer keys within a certain range.
# Dictionaries can be indexed in the same way as lists, using square brackets
# containing keys.
# Example:

print("\n\n Excercise #1 - Dictionary mapping person to age")

ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

# Each element in a dictionary is represented by a key:value pair.


print("\n\n Excercise #2 - Printing a key which is not part of a dictionary \n")
# Trying to index a key that isn't part of the dictionary returns a KeyError.

primary = {
"red": [255, 0, 0],
"green": [0, 255, 0],
"blue": [0, 0, 255]
}

print(primary["red"])
#print(primary["yellow"])

# a dictionary can store any types of data as values.
# An empty dictionary is defined as {}.

print("\n\n Using a mutable object as dictionary returns a TypeError \n")

# Only immutable objects can be used as keys to dictionaries.
# Immutable objects are those that can't be changed. So far, the only mutable
# objects you've come across are lists and dictionaries. Trying to use a mutable
# object as a dictionary key causes a TypeError.

bad_dict = {
[1, 2, 3]: "one two three",
}

# One way to test whether a variable is mutable or not is to copy it to a new variable, then change the first variable:
# > a = 8
# > b = a
# > a += 2
# > print(a)
# 10
# > print(b)
# 8
# > # Integers are immutable, since a change to 'a' was not a change in 'b'.
#
# > a = "hello"
# > b = a
# > a = "goodbye"
# > print(a)
# "goodbye"
# > print(b)
# "hello"
# > # Strings are immutable, since a change to 'a' was not a change in 'b'.
#
# > a = ['do', 're', 'mi']
# > b = a
# > a.append('fa')
# > print(a)
# ['do', 're', 'mi', 'fa']
# > print(b)
# ['do', 're', 'mi', 'fa']
# > # Lists are mutable, since a change to 'a' was also a change to 'b'.

# Here's the list of class that are immutable:
#
# 1. Bool
# 2. int
# 3. float
# 4. tuple
# 5. str
# 6. frozen set
#
# And Here's the list of class that are mutable:
#
# 1. list
# 2.set
# 3.dict
