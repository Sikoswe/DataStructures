# Loops
# What is a loop

. A Loop is any repeated statement or task more than one time until ataining the paticular condition.

# Importance of loops

- Loops helps us remove the redundancy of code when a task has to be repeated many times. 
- Loops cane cut hundreds of lines of code into few by making use of loops, rather than writing a print statement 8 times, you just indicate the number of repetitionions you want. 
- Basically here are three types of loops;
. While loop
. For loop
. Nested loop

# While loop

. A while loop is a type of loop tha consistently reads the proclamation code whenever it gives back a true feedback to a given condition. It is also known as entry control loop because the test-expression is evaluated before entering into a loop.
. It allows total number of repitations to be unknown from the start.

Its syntax
          while test_condition:       boolin condition evaluation
          statement()                  body execution

    example
- Print 15 moos. Than wring the program again and again we can write it in an advanced way.

print("moo")
print("moo")
print("moo")
print("moo")                                          for i in range(15):
print("moo")           instead we use loops                print("moo")
print("moo")
print("moo")
print("moo")
print("moo")
print("moo")
print("moo")
print("moo")                                     
print("moo")           
print("moo")

when you run this code you’ll notice that the program moos 15 times in the terminal as an outcome.
- At this point a while statement is more like an if statement, if the condition is not false it keeps on checking on it. If the condition is never false the loop runs forever until it runs out of memory.

    example2

count = 0
while count < 5:
    print("fail")
    print("not happy")

- The program will forever be running because the given condition is true and can never be false if not edited to false, this loop is not an ifinity

      example3
 
 - Print the multplication table of numbers 1 to 10.
 - We shoud create a loop that runs from 1 to 10

number = int(input("enter a number:"))
count = 1
while count <= 10:
    product = number * count
    print(number, "x", count, "=", product)
    count = count + 1 

- When run it will shows the multplication table in a well arranged manor