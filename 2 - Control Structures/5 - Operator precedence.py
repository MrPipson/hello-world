# Operator precedence is a very important concept in programming. It is an extension
# of the mathematical idea of order of operations (multiplication being performed before
# addition, etc.) to include other operators, such as those in Boolean logic.
# The below code shows that == has a higher precedence than or:

print(False == False or True)
print(False == (False or True))
