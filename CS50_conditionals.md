# CS50 conditionals

Conditional statements are expressions that allows the programer to make ddecitions and take different angle in the road, depending on the vaues of variables or user input.
-Conditional statements works with mathematical symbols that plays a role of asking questions.
Symbols like; 
<  greater than symbol
<=  greater than or equal to symbol
>  less that symbol
>= less than or equal to symbol 
== equal to compirering two things left to right 
!= not equal to  

the conditional always compires the right given 
 
 # If statement/ elif-else 

 -If statement plays a role of providing decitions in order to direct the programer to provide result based on a specified standards. We can have an example of our daily usual talks, if i get sick then i will go to the hospital, if not i will wont. It always goes with two posible outcomes. eg

if heart beat = 45
if heart beat > 40:
    print("it's warm")
    print("drink water")

    print("done")
if you want to have multyple conditions we you an elif statement where el is short of else 

elif heart beat > 30:
    print("it's nice")
      if true
else: 
    print("it's normal")  
print("done")

  example 2

In this case i have two variables a and b for each one of them has its own values. For me to have a decision on my variables, i have to bring up if function and a mathematical symbol to ask the question the other way round. Int will turn the laters of my variables to its character as integer

      a =int(input("what's a? "))
      b =int(input("what's b? "))
       if a < b:
       print("a is less than b")
             same as
       if 1 < 2:
       ....print ("a is less than b")
       meaning ("1 < 2")

        print("a is less than b ")
If statements use a pair of true or false which is a boolin to decide whether or not to execute. If the statement of a b is true, the compiler will register it as true and execute the code.

-We can also represent our program using a flow chart representation which is a schematic diagram that uses special symbols in order to organise the facts.
-it starts with the word start in a rounded rectangle or oval shape, where all the idears starts
-the next step is an input stage where operaations are placed in parallelogram eg (x < y). it is where boolin questions are asked is x < y? if yes then go to the left if no go to the right, if really true it will print ("x is less than y"). it will again ask the question for the second time
, is x > y? and display the fact ("x is greter than y")

# or

we can also use or that allows your program to decide between one or more alternatives. For example, we could further edit our program as follows:

a = 10
b = 10
c = 0

if a > b or b > 0:
   print("either of the number is greater than 0")
else:
   print(""no number is greater than 0)
if b > 0 or c > 0:
    pront("either of the number is greater than 0")
else:
    print("no number is greater than 0")

-Either of the number is greater than 0 no  number is greater than 0
-if the first expression evaluated to be true while usin or operator, then the feather expressions are not evaluated.

# And

- And conditional is also used within conditional statements to help additioning the gigen program.
Start a new program.  logical operator returns true if both the operands are true else it turns folse.
     examlpe 1

a = 12
b = 12
c = -12

if a > 0 and b < 0:
     print("the numbers are greater than 0")
if a > 0 and b > 0 and c > 0:
     print("the numbers are graeter than 0")
else:
     print("at lest one number is not greater than 0")

# Modulo

-In mathematics a modulo or modulas, mod in python is the remender after dividing two numbers. The term modulo is often used to assert that two distinct mathematical objects that can be regarded as equivalent if their difference is accounted for by an additional factor.
-In python modulus symbol is is represented as the percentage (%) symbol. Through this, it as called the remender operator. 
                Example of a modulo we can say:

        15 mod 12 = 3    meaning our modulo is 3
        15 % 12 == 3

                Example2

x = int(input("What's a? "))

if a % 4 == 0:
    print("Even")
else:
    print("Odd")
You can type in any number 1 or greater than 1 to see if it is an even or odd number.

# Creating Our Own Parity Function

-We can create our own function to check whether x is a member of A or B. We can whrite our program follows:

def main():
    A = ("v, w, x, y, z")
    B = ("v, y, z")
    if x is a member of A:
        print("member")
    else:
        print("not a member")

# Pythonic

In programming, there are types of programming that are called “Pythonic” in nature. That is, there are ways to program that are sometimes only seen in Python programming. Consider the following revision to our program:

    def main():
    A = int(input("v, w, x, y, z"))
    B = int(inptut("v, y, z"))
    if x is a member of A:
        print("member")
    else:
        print("not a member")    


def is a member:
    return True if n % 2 == 0 else False

main()
Notice that this output statement of our program is almost like a sentence in English. This is a matchless way of coding only seen in Python.

We can further revise our code and make it more and more readable:

def main():
    A = int(input("v, w, x, y, z"))
    B = int(inptut("v, y, z"))
    if x is a member of A:
        print("member")
    else:
        print("not a member")

def is a member:
    return n % 2 == 0

main()
The program will apraise what is happening within the n % 2 == 0 as either true or false and simply return that to the main function.#

          
      




