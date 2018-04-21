# List slices provide a more advanced way of retrieving values from a list.
# Basic list slicing involves indexing a list with two colon-separated integers.
# This returns a new list containing all the values in the old list between the indices.
# Example:

print("\n\n Excercise #1 - Print parts of the list specifying the x:y range - x included, y excluded \n")

print(" [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] ")
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(" [2:6] ")
print(squares[2:6])
print(" [3:8]")
print(squares[3:8])
print(" [0:1]")
print(squares[0:1])

# Like the arguments to range, the first index provided in a slice is included
# in the result, but the second isn't.

# If the first number in a slice is omitted, it is taken to be the start of the list.
# If the second number is omitted, it is taken to be the end.
# Example:

print("\n\n Omitting the first/last number in the slice \n")

print(" [:7] ")
print(squares[:7])
print(" [7:]")
print(squares[7:])

# Slicing can also be done on tuples.
