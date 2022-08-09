# Loops

. Looping means repeating something time and time again untill the paticular condition is satisfied.
. We start by creating a file name, cow.py which produces a sound of (moo) in the terminal window.
. In the text editor, begin with the following code:

print("moo")
print("moo")
print("moo")
print("moo")
Running this code by typing python cow.py, you’ll notice that the program moos four times.

# While loop

. A while loop in python sets aside a block that is to be executed again and again untill a condition gets upto its requared leval.
. It allows total number of repitations to be unknown from the start

# stuff before the while loop, e.g.:

count = 0

condition = lambda x: x <= 5

 

while condition(count): # note the colon, which is required

    # an indent of four spaces or 1 tab is required

 

    # stuff that will be executed until condition is False, e.g.:

    print('The count is', count) # this works in Python 3 or higher

    

    # update the condition so it becomes false eventually

    count += 1 # this adds one to count and re-assigns it to count

 

# stuff after the loop: (no more indent)

print('while loop done')