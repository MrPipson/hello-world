# Functions
#
# In addition to using pre-defined functions, you can create your own functions
# by using the def statement.
# Here is an example of a function named my_func. It takes no arguments, and
# prints "spam" three times. It is defined, and then called.
# The statements in the function are executed only when the function is called.

def my_func():
    print("spam")
    print("spam")
    print("Spam")

my_func()

# The code block within every function starts with a colon (:) and is indented.

# You must define functions before they are called, in the same way that you must
# assign variables before using them.

hello() #causes a NameError since hello function is not defined

def hello():
    print("Hello world")
