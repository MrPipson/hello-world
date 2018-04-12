# An if statement is run once if its condition evaluates to True, and never if it evaluates to False.
# A while statement is similar, except that it can be run more than once. The statements inside it are
# repeatedly executed, as long as the condition holds. Once it evaluates to False, the next section of
# code is executed.
# Below is a while loop containing a variable that counts up from 1 to 5, at which point the loop terminates.

i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Finished")

# The infinite loop is a special kind of while loop; it never stops running. Its condition always remains True.
# An example of an infinite loop:

# while 1 == 1:
#     print("In the loop")

# You can stop the program's execution by using the Ctrl-C shortcut or by closing the program.

# To end a while loop prematurely, the break statement can be used.
# When encountered inside a loop, the break statement causes the loop to finish immediately.

i = 0
while 1 == 1:
    print(i)
    i += 1
    if i >= 5:
        print("Breaking")
        break
print("Finished")

# Using the break statement outside of a loop causes an error.

# Another statement that can be used within loops is continue.
# Unlike break, continue jumps back to the top of the loop, rather than stopping it.

i = 0
while True:
    i += 1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print ("Breaking")
        break
    print(i)

print("Finished")
