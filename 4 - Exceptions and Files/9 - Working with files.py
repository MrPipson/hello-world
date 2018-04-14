print("\n\n Excercise #1 - Make sure files are closed trough try and finnally \n")
# It is a good practice to avoid wasting resources by making sure the files are
# always closed after they have been used. One way of oding this is to use try and finnally

try:
    f = open("testnew.txt")
    print(f.read())
finally:
    f.close()

# this ensures that the file is always closed even if  an error occurs

print("\n\n Excercise #2 - Using with stataments with files to automatically close them \n")
# An altetnrative way of making sure file is closed is using with statements.
# This creates a temporary variable (often called f), which is only accessible
# in the indeted block of the with statement

with open("testnew.txt") as f:
    print(f.read())

# The file is automatically closed at the end of the with statement even if
# exceptions occur with it


# EXTRA TIPS IN USING FILES:
#
# How to rename a file in python:
# import os
# os.rename(old_file.txt,new_file.txt)
#
# # os is a module to manipulate
#    operating system and the rename
#    function would allow to rename
#    files into a new one.
#
# how to delete a file:
# import os
# os.remove(file.txt)
#
# # the remove function would allow it
#     to delete a file that is inputted.
