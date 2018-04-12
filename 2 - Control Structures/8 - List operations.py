# The item at a certain index in a list can be reassigned.

nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

# Lists can be added and multiplied in the same way as strings.

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

# Lists and strings are similar in many ways - strings can be thought of as lists of characters that can't be changed.

# To check if an item is in a list, the in operator can be used. It returns True
# if the item occurs one or more times in the list, and False if it doesn't.

words = ["spam", "egg", "spam", "saussage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

# To check if an item is not in a list, you can use the not operator in one of the following ways:

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)
