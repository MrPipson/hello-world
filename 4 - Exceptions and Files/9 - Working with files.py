print("\n\n Excercise #1 - Make sure files are closed trough try and finnally \n")
# It is a good practice to avoid wasting resources by making sure the files are
# always closed after they have been used. One way of oding this is to use try and finnally

try:
    f = open("testnew.txt")
    print(f.read())
finally:
    f.close()

# this ensures that the file is always closed even if  an error occurs
