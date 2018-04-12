# the contentsof a file that has been opened in the text mode can be read using
# the read method

file = open("test.csv", "r")
cont = file.read()
print(cont)
file.close()

# this will print all the contents of test.csv

# To read only a certain amount of a file, you can provide a number as an argument
# to the read function. This determines the number of bytes that should be read.
# You can make more calls to read on the same file object to read more of the file
# byte by byte. With no argument, read returns the rest of the file.

file = open("test.csv", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

# After all contents in a file have been read, any attempts to read further from
# that file will return an empty string, because you are trying to read from the
# end of the file.

file = open("test.csv", "r")
file.read()
print("Re-reading...")
print(file.read())
print("Finished reading")
file.close()

# how to open a file, read its contents and print its lenght

file = open("test.csv", "r")
str = file.read()
print(len(str))
file.close()


# to retrieve each line in a file, you can use the readlines method to returns
# a list in hich each element is a line in the file

file = open("test.csv", "r")
print(file.readlines())
file.close

# you can also use a for loop to iterate trhough the lines in the file

file = open("test.csv", "r")
for line in file:
    print(line)
file.close()

# In the output, the lines are separated by blank lines, as the print function
# automatically adds a new line at the end of its output.

# Python automatically reads files by lines. It reads text by characters.
# So if we were to say text = file.read() first and then put text in the for loop instead, it would go by character, which is what you'll often want to do
# As the file is in the for loop, however, Python reads it line by line.
