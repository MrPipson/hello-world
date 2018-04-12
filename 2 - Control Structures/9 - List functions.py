# Another way of altering lists is using the append method.
# This adds an item to the end of an existing list.

nums = [1, 2, 3]
nums.append(4)
print(nums)

# The dot before append is there because it is a method of the list class.
# Methods will be explained in a later lesson.

# To get the number of items in a list, you can use the len function.

nums = [1, 2, 3, 4, 5]
print(nums)
print(len(nums))

# The insert method is similar to append, except that it allows you to insert
# a new item at any position in the list, as opposed to just at the end.

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

# There is no need to use index, just enter words.insert(1,"is") , you can use
# any number in place of 1 for insert in that position. e.g words.insert(2,"is")
# it will insert "is" second position

# You can even insert an index of a negative number, then the function will count from right to left in the list. For example,

nums = [2, 7, 4, 3, 0]
nums.insert(-1, 5)
print(nums)

# The output will be [2, 7, 4, 3, 5, 0]
# The inserted number 5 now stands at the -1st position in the list.

# The index method finds the first occurrence of a list item and returns its index.
# If the item isn't in the list, it raises a ValueError.

letters = ['p', 'q', 'r', 's', 't']
print(letters.index('r'))
print(letters.index('p'))
# print(letters.index('z'))

# There are a few more useful functions and methods for lists.
# max(list): Returns the list item with the maximum value
# min(list): Returns the list item with minimum value
# list.count(obj): Returns a count of how many times an item occurs in a list
# list.remove(obj): Removes an object from a list
# list.reverse(): Reverses objects in a list

letters = ['p','A', 'q', 'r','u','k','h','s', 'p', 'u','z','Z']
print(letters)
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('u'))
print (max(letters ))
print (min(letters ))
print (letters.count('p'))
print (letters.count('Z'))
letters.remove('A')
print (letters )
letters.reverse()
print (letters )
print (letters.count('p'))
print (max(letters ))
print (min(letters ))


hello = [1, 2, 3, 3, 4, 5]

max(hello) #[Returns 5]
#max(list) #returns the item with the greatest value, example: The Largest number and alphabetically Least to Greatest

words = ['hello','world','and','hello','universe']
max(words) #[returns 'world']
#=============================================================
min(hello) #[Returns 1]
min(words) #[Returns 'and']

#min(list) is just the Vice Versa of max(list)--it [min(list)] returns the item with the least value,
#example: The smallest number and alphabetically Greatest to Least.
#=============================================================
hello.count(3) #[Returns 2]
words.count(hello) #[Returns 2]

# listName.count(item) Returns how many times the item in the list is Repeated.
#=============================================================
hello.remove(3) #[Removes a '3']
words.remove('and') #[Removes 'and']
