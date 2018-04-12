# The range function creates a sequential list of numbers.
# The code below generates a list containing all of the integers, up to 10.

numbers = list(range(10))
print(numbers)

# The call to list is necessary because range by itself creates a range object,
# and this must be converted to a list if you want to use it as one.

# Range differs from a List because a range object stores only start, end, step
# instead of individual elements whereas a list object actually saves each elements.
# In the case of large sequential integer elements, range uses little memory comparing to list.
# When you want to explicitly see what a range object represents, convert to list and print it.

nums = list(range(5))
print(nums) #output is [0, 1, 2, 3, 4]
print(nums[4]) #output is 4

# If range is called with one argument, it produces an object with values from 0 to that argument.
# If it is called with two arguments, it produces values from the first to the second.

numbers = list(range(3, 8))
print(numbers) #output is [3, 4, 5, 6, 7] -> len(range(x,y)) is y-x

print(range(20) == range(0, 20))

# range can have a third argument, which determines the interval (step) of the sequence
# produced. This third argument must be an integer.

numbers = list(range(5, 20, 5))
print(numbers) #output is [5, 10, 15] a list starting with 5 and incrementing by 2 until 20 (excluding 20)
