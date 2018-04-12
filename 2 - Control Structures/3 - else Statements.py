# An else statement follows an if statement, and contains code that is called
# when the if statement evaluates to False.

m = input("Input a number: ")
if int(m) == 4:
    print("m is a four")
else:
    print("m is not a four")


# else statement can be used to test series of conditions:
y = input("Input a number to test: ")
x = int(y)
if x == 7:
    print("Number is 7")
else:
    if x == 8:
        print("Number is 8")
    else:
        if x == 5:
            print("Number is 5")
        else:
            print("Number is not 7, 8 nor 5")

# elif Statements
# The elif (short for else if) statement is a shortcut to use when chaining if and else statements.
# A series of if elif statements can have a final else block, which is called if none of the if or elif expressions is True.

z = input("Input a number to test: ")
a = int(z)
if x == 5:
    print(5)
elif x == 4:
    print(4)
elif x == 3:
    print(3)
else:
    print("It is not a 5, 4 nor 3")
    
