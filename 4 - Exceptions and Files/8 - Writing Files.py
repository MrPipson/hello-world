
print("\n\n Excercise #1 - Writing to a file and reading it: \n")
# To write to files you use the write method, which writes a string to the file.
# For example:

file = open("testnew.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("testnew.txt", "r")
print(file.read())
file.close()

# The "w" mode will create a file, if it does not already exist.
# N.B: When a file is opened in write mode, the file's existing content is deleted.

print("\n\n Excercise #2 - Overwritting a file: \n")

file = open("testnew.txt", "r")
print("- Reading and printing original file contents:")
print(file.read())
print("- Finished with original file")
file.close()

print("- Open in write mode and write some new text")
file = open("testnew.txt", "w")
file.write("Some new text I've written")
file.close()

file = open("testnew.txt", "r")
print("- Reading and printing new file contents:")
print(file.read())
print("- Finished reading and printing new file contents")
file.close()

# As you can see, the content of the file has been overwritten.
# If you open a file in write mode and immediatelly close it, all contents will
# be deleted!

print("\n\n Excercise #3 - Write method retunrs bytes written\n")
# The write method returns the number of bytes written to a file if successful
# this statement will be true: file.write(msg) == len(msg)

msg = "hello world!"
file = open("testnew.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
