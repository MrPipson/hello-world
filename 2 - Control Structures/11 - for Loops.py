# Sometimes, you need to perform code on each item in a list.
# This is called iteration, and it can be accomplished with a while loop and
# a counter variable.

#ITERATION WITH WHILE LOOP

words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
    word = words[counter]
    print(word + "!")
    counter = counter + 1

# The example above iterates through all items in the list, accesses them using
# their indices, and prints them with exclamation marks.

#ITERATION WITH FOR LOOP

# Iterating through a list using a while loop requires quite a lot of code,
# so Python provides the for loop as a shortcut that accomplishes the same thing.
# The same code from the previous example can be written with a for loop, as follows:

words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

# The for loop is commonly used to repeat some code a certain number of times.
# This is done by combining for loops with range objects.

for i in range(5):
    print("Hello") #output is 5 entries of "Hello"

# You don't need to call list on the range object when it is used in a for loop,
# because it isn't being indexed, so a list isn't required.

#create a loop that prints only even numbers within a range

for i in (range(0,20,2)):
    print(i)
    
