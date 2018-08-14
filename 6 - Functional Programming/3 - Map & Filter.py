# The built-in functions map and filter are very useful higher-order functions that operate on lists (or similar objects called iterables).
# The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
results = list(map(add_five, nums))
print(results)

# The same result can be achieved by using the lambda syntax:

nums = [11, 22, 33, 44, 55]
results = list(map(lambda x: x + 5, nums))
print(results)

# the function filter filters an iterable by removing the items that dont match a predicate (a function that returns a boolean)

nums = [11, 22, 33, 44, 55]
results = list(filter(lambda x: x%2==0, nums))
print(results)

# Like map, the result has to be explicitly converted to a list if you want to print it.
