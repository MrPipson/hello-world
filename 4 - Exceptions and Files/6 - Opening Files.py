# You can use Python to read and write the contents of files.
# Text files are the easiest to manipulate. Before a file can be edited,
# it must be opened, using the open function.

myfile = open("C:\\Users\\Djordje\\Documents\\Python\\Finance\\aapl-test.csv")

# myfile = open("filename.txt") if in the same directory

# The argument of the open function is the path to the file.
# If the file is in the current working directory of the program, you can specify
# only its name.

# You can specify the mode used to open a file by applying a second argument to the open function.
# Sending "r" means open in read mode, which is the default.
# Sending "w" means write mode, for rewriting the contents of a file.
# Sending "a" means append mode, for adding new content to the end of the file.
#
# Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
# For example:

# write mode
open("test.csv", "w") #for reqriting the contents of the file

# read mode
open("test.csv", "r")
open("test.csv") # default is read mode

# binary write mode - for openin png or sound files for example
open("test.csv", "wb")

# FILE MODES:
#
# "r"
# Read from file - YES
# Write to file - NO
# Create file if not exists - NO
# Truncate file to zero length - NO
# Cursor position - BEGINNING
#
# "r+"
# Read from file - YES
# Write to file - YES
# Create file if not exists - NO
# Truncate file to zero length - NO
# Cursor position - BEGINNING
#
# "w"
# Read from file - NO
# Write to file - YES
# Create file if not exists - YES
# Truncate file to zero length - YES
# Cursor position - BEGINNING
#
# "w+"
# Read from file - YES
# Write to file - YES
# Create file if not exists - YES
# Truncate file to zero length - YES
# Cursor position - BEGINNING
#
# "a"
# Read from file - NO
# Write to file - YES
# Create file if not exists - YES
# Truncate file to zero length - NO
# Cursor position - END
#
# "a+"
# Read from file - YES
# Write to file - YES
# Create file if not exists - YES
# Truncate file to zero length - NO
# Cursor position - END

# Once the file is opened, it should be closed once done. This is done
# with the close method of the file object

file = open("test.csv", "w")
# do stuff to the file
file.close()
