# List comprehensions are a useful way of quickly creating lists whose contents
# obey a simple rule.
# For example, we can do the following:

print("A list comprenehsion for creating a list of cubed numbers \n")

cubes = [i**3 for i in range(5)]
print(cubes)


# List comprehensions are inspired by set-builder notation in mathematics.

# A list comprehension can also contain an if statement to enforce a condition
# on values in the list.
# Example

evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

# Trying to create a list in a very extensive range will result in a MemoryError.
# This code shows an example where the list comprehension runs out of memory.

# even = [2*i for i in range(10**100)]

# This issue is solved by generators, which are covered in the next module.
