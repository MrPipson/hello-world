# You can use if statements to run code if a certain condition holds.
# If an expression evaluates to True, some statements are carried out.
# Otherwise, they aren't carried out.
'''
if expression:
   statements # Python uses indentation
'''

if 10 > 5:
    print("Ten greater than five")
print("Program ended.")

# To perform more complex checks, if statements can be nested, one inside the other.
# This means that the inner if statement is the statement part of the outer one.
# This is one way to see whether multiple conditions are satisfied.

num = 12
if num > 10:
    print("The number is bigger than 10")
    if num < 20:
        print("The number is between 10 and 20")

#if the expression is not satisfied, the inner statement will not run

num = 6
if num < 12:
    print("I will not run next if and will print 2")
    if num < 5:
        print(6)
        if num == 6:
            print("it is a six")
