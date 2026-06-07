# Welcome to python.
# Our purpose here is to learn python from ground zero.
"""
    Used variable-
    x-user's name
    y-Name of the user's mother
    area-Where does she lives?
"""
# Ask user for their name
x = input("What's your name buddy? " )
# We are adding the input into the variable
# Saying hello
print("hello,")
print(x)
# But this way their is gap on the introduction
"""
    another way of adding a comments
    the output will be like_
    hello
    _____
"""
""""
what we have to do is do primt("hello" + the variable)
This way their will be no gap..
the output will be like_
 hello _____
"""
print("Nice to meet you" + x)
"""
    But this time the output is like_
    "Nice to meet you tamjid"
    we can add a space ourselves like "print("nice to meet you " + x)"
    We cam see that there is no space between the printed text and the variable.
    So what we have to do is use another operator. We are going to use"," instead of the "+"

"""
#This time the "," operator automatically adds the space between the printed text and the input

print("Nice to meet you" , x)

#another way to solve this problem is ' end="/n" ' this attribute means the output will go to the next line immidiately
#If we use ' end="" ' then it'll mean the next input will be in the same line.
"""
    What we are going to use as the input is_
        print("Nice to meet you" , end="")
        print(x)

"""
print("Nice to meet you " , end="")
print(x)
"""
This time the "," operator is used in using not just one but two arguements in the print function recall that they magically had a space betweem them
Also it adds the needed space by deffault
"""
print("Nice to meet you " , end="??")
print(x)

print("Nice to meet you " , end="123" )
print(x)

"""
    actual use of end=""_
        It actually means the next line of the program will be printed at the line.
        if we just use end="", then we wont find any space between them.
        But if we use end=" ", then we will find a space.
        If we use end="123", then we will find 123 between them.
        Also if we want to use end="" but still we want to make a separate line, then we have to use end="/n"
"""

#We can use both ""/'' ..in python it doesm't matter

# How to use qoute
# as we know that in puthon is doesn't matter if we usse "" or not ... we can use "''"
#it doesn' matter

print(x + ' said, "he is not good guy"' )
print(x , 'said, "he is not good guy"' )

"""
    We can also use it this way_
        print("he said,\"friend\"")

"""
print(x , "said,\"Bum diki diki bum bum\"")

#let's get back to the introduction
"""
we can use the variable inside the "". Here is how we do it_
    print("hello{x}")
    [We are gonna see a difference. Which indicates, by this python will know that something is going on in the second bracket ]. But still it won't print what we need.
What we have to is_
    print(f"hello, {x}")
"""
print(f"hello {x}")

#Now we are going to strip our output
"""
    What we are going to do is use a new arguemnt which is called "str"
    If we use the usual attibute, then the output will be usual but it doesn't look good sometimes.
"""
#If we use_
x = x.strip()
print(f"Hello, {x}")
#Now if we give our input with too many spaces then the output will also be with those too many spaces which doen't look goos
#So what we are going to do is type_ [x = x.strip()]
print(f"Hello, {x}")

#capitalize user's name
"""
    x = x.capitalize()
    This function actually capitalizes the first letter

"""
x = x.capitalize()
print(f"Hello, {x}")

"""
    But we are kinda being tired typing all these lines off code ...So we want to combine those codes together and make a single line code
    We are going to use _
    x = x.strip().title()
 """

print('''I am tamjid
       I study in cuet ''')

# By ('''ABD ''') It'll print the same way

# We can use it as a substitute of the format functions

x = input("What's your name? ").strip("-")
print(f"Hello, {x}")


x = x.strip().title()
print(f"Hello, {x}")
#we can make this step even further... We can use this caode directly while we are taking input

#Let's take another input
#We are taking another variable "y"

y = input("What's your mother's name?").strip().title()
print(f"Really? {y}? I know her ....she's great..")

#Let's think about a simple thing, when we introdyce ourselves to someone and they tell us their name we don't talk to tem y their name. We use their first name or their nickname.
#So, we have to make our program to do the same.
"""
    This time we are going to use a new attribute which is called split(" ")

"""

#Split user's first and last name
first, last = y.split(" ")

#Saying hello to the new user
area = input(f"Well, where does yur mother Mr.s {first} lives?").title()

#Use of integer (it is used for mathamatical equations)
"""
    Python allows you to add these symbols and more_
    +  adding number
    -  subtract number
    *  multiple numbers
    /  devide numbers
    %  It's a operator called "modulo" that allows you to take the remainder after deviding one number by another.

"""
#calculator
#We are going to enable to mathamatical signs by the "int" function
#Without the "int" function the sign will be used as texts as usual.

#First we are to take the input from the users.

A = input("what is x? ")
B = input("what is y? ")

z = int(A) + int(B)
print(z)

#But if we use a variable just one time then there no reason to make a variable. Because we are going to make a variable but we'll use it only once.
#So, we are going to try use the function without making the variable.

a = int(input("a=? "))
b = int(input("b=? "))

print( a+b )

#We could've wrote the code like_ print( int(input("a=? ")) + int(input("b=? ")) )
"""
    But we didn't. Because the more short we make the code we are ourselves think too much.
    Anytime we make ourselves think we're wasting time and anytime we complicate the look of the code like this,
    we are just going to increase the probability of mistakes or logical errors in our code

"""
#To add floating point values too.. we have to use a new attribute "float"
#We need the floating attribute because we are not expectung only integer numbers from the users.
#We can actually do floating point arithmetic as well.

c = float(input("What's x? "))
d = float(input("What's y? "))
print(c + d)
#Round the number the nearest integer number.
#We are using another function to make the result to the nearest possible integer for instance.
"""
round(number[, ndigits])
    This is what the function looks like in the documentation of python.
        The name of the function is of course "round" and it's first arguement is a number. But in programming language when we see
        square brackets, it means that we are about to see something optional and so what this means is if you want to specify more precisely the number of digits
        that you want the round function to round two you specify it here by adding a comma and then that number.
    So if we read the documentation if you don't specify a number of digits you just specify the number to round it, it rounds to the nearest integer.
        But suppose we want it round to the tenths place or the hundredths place that is one pr two digits after the decimal point we additionally pass im  ", 1"/", 2" to be more precise.
"""
print(round(c + d))
#But usually we may find ourselves losted trying to make a single line code, as we said before.
#So, we are going to simplify things with variables.

v = round( c + d )
print(v)

#  Let's say we do "999+1=1000" But we usually use it with comma. Like 1,0000
#There is a way in python to specify that we want to include comma in our numbers like this.

#We are going to use our old function "f". Then we're going to use "'variable':,"
print(f"{v:,}")

#Let's make a division.
print(c/d)
#But we want to round the answer so we are going to make our to round the number. So we are going to use the "round" function and also we going to pass in 2 so that I can specify n digits number which recall was the second perameter for round.

print(round(c/d, 3))

#Let's make our comma uddy to come in our program.
m = round(c/d, 3)
print(f"{m:,}")
#creating our own function
"""
    We've already wrote 212 lines of code and we have to use 'print("hello")' a lot. Wouldn't it be nice if we could make a special function which is only used for printing "Hello"
    That's where our new function "def" comes.
    def is for define. If and when we want to define, create our own functions we can do so using now this keyword in python.
"""
"""
 if we use_
    name = input("what's your name? ")
    hello()
    print(name)

But it is not going to work. Because we haven't defined our function "hello()"

"""


"""
    It means we're saying first we are defining a function. Then we"re putting the input into the function
    What our program is going to do is_
            1. Our input will be taken by the program.
            2. Then hello(f)..here f is kind of a variable..(it's easy to understand)
            3. We print("hello", f)..here it'll print Hello and then i'll print our input.
               Here, our "name" variable is going to take place of "f"

"""
def hello(f):
    print("Hello,", f)

name = input("What's you name? ")
hello(name)

def Hello(to="world"):
    print("hello,", to)
Hello()
#   Here the program is going to greet "world" instead of the user, because we didn't put anythng in the "Hello(_)"
#   Because at first we put "to="world"". So the program is automatically going to put "world"
Name = input("What's your name? ")
Hello(Name)

def main():
    name = input("What's your name? ")
    HELLO(name)

def HELLO(to="Boom"):
    print("HeLLo,", to)

main()

"""
  What's happening is is we're defining a function 'main()' then we're defining another function called 'HELLO'. How this is going to work is
  if we call the 'main()' function, then automatically the 'HELLO' function is going to work.
    def main():
    name = input("What's your name? ")
    HELLO(name)

    def HELLO(to="Boom"):
    print("HeLLo,", to)      Here firstly we're defining the functions then,

    main()                   Here we are actually enabling the program by promgam.
"""
#We can also use it in a different way.
#If we type in_ return n ** 2 ...the result will be the same.
# by doing that python means that n = the given number; ** = to the power; 2 = the power on the right.

 #We can also get the same output by a new function. "pow"

def main():
    x = float(input("What's the value of x you want to do square? "))
    print("x squard is", square(x))

def square(n):
     return pow(n, 2)
main()

#New functions_
"""
    > - Greater tham
    >= - Greater than / equal to
    < -  Less than
    <= - Less than / equal to
    == - Equal
    != - Not equal
"""

#The if/elif/else_
x = input("What's the value of x?")
y = input("What's the value of y?")
if x>y:
    print("x is greater than y.")
elif x<y:
    print("x is less than x.")
else:
    print("x is equal to y")


#Here we are using a alphatical variable. So we have to use cotation marks to defne the alphabatical input.
x = "waziha"
y = input("What's your name? ")

if x.lower() == y.lower():
    print("Welcome to your PC, sir. How may I help you?")
else:
    print("What are you doing on Waziha's laptop? It's her laptop. Please return it to her as soon as possible.")
#We added the .lower() method to both x and y when comparing them. This ensures that the comparison is case-insensitive. Therefore, whether the user inputs "Tamjid", "tamjid", or any other variation of the name, it will be considered a match.
#Though if we don't use it, it wouldn't be a problem.

#And functions
# Here we are saying to the program if the input is greater than or equal to 33 and it's less than or equal to 39 then we are going to print "D"

score = float(input("Your score: "))

if score >= 90 and score <= 100:
    print("Grade: Golden A+")
elif score >= 80  and score <= 89:
    print("Grade: A+")
elif score >= 70  and score <= 79:
    print("Grade: A")
elif score >= 60  and score <= 69:
    print("Grade: A-")
elif score >= 50  and score <= 59:
    print("Grade: B")
elif score >= 40  and score <= 49:
    print("Grade: C")
elif score >= 33  and score <= 39:
    print("Grade: D")
else:
    print("F")

# We could also use it like this _
"""
if 33 <= score <= 39
print("Grade: D")
"""
"""
    Also we could use it more simply.
    if score >= 90:
        print("Grade: Golden A+")
    elif score >= 80:
        print("Grade: A+")

    But right here we must use the "elif" we can't use "if".
    If we use "if", Then it'll print every grade because i'll be good with every given demands.
"""

 # Introduction to OR function
x = int(input("What's your age? "))
if x < 0 or x > 0:
    print("X is not equal to 0")
else:
    print("X is equal to 0")
# We could also use "x != 0". Then we wouldn't have to use the Or function.

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# We can also use it as, " return True if n % 2 == else False "
"""
    We can also use just "return n % 2 == 0".
    Because the expression return itself has a true or false answer.
    Then why are we asking True or False again? We can just return the value of our own Boolean expression.
    That is why we can just return n % 2 == 0. We don't need to wrap it with if and else.
    So this is the most elegant way to implement this same idea.
"""
"""
def is_even(n):
    return True if n % 2 == 0 else False
"""
"""
def is_even(n):
    return n % 2 == 0
"""

main()

# Introduction to "match"
# Match is a a mechanism that if you've programmed before is similar in spirit to something called switch in oter languages.

# Let's implement a program that prompts the user for their name and it just outputs what house they're known to be in the world of "Harry Potter"\

# let's give ourselves a variable called "name" equal to the return value to the input function.
# After that we are going to use simple if elif else functions to decide what house this person is in.

name = input("What's your name wizard? ").title()


if name == 'Harry' or name == 'Hermione' or name == 'Ron':
    print("Gryffindor")
elif name == 'Draco':
    print("Slytherin")
else:
    print("Who? ")

"""
    We can imagine how difficult and hard the code would be if It was not only just 3 names.

"""
# This is where we will use a whole different code.
# We will use the function match


name = input("What's your name? ").title()

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Not in the school.")

# We can use it other way instead of listing out the names individually.
# We can use "case 'Harry' | 'Hermione' | 'Ron' "

name = input("What's your name? ").title()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Not in the school.")


# Intoduction to loops

i = 0
while i < 3:
    print("meow")
    i = i + 1

# Instead of using i = i + 1, we can use i += 1. It means the same thing.

# We can use the "for" loop as well and it kind of simplifies the things.
# If we take a variable like "i" a number and we know in advance how many times we want this Loo[ to execute, 3 tmes.
"""
   In this loop we want python to take input as i is 0. Then "meow" will be printed.
   And then python will update itself and then i will be equal to 1, then meow. then 2 then meow, then stop.
   The square brackets represents list.
"""
for i in [0, 1, 2]:
    print("meow")
# Then what if we want to print it a million times. Are we going to type in [1,2,3,...1000000]?
# No. We are going to use a new function called range()

for i in range(3):
    print("meow")
"""
    By specifying range three we're essentially being handed back 1,2,3. By default those values are [0,1,2].
    But what is brilliant about this is that now to Hope's point if I do want to meow a million times. We can just type a million.
    We don't necessarily want to a variable like "i". There is convention in Python wherewe need variable just because just because the programming feature requires it to do some kind of counting or automatic updating but we the human don't care about its value a pythonic inprovement here would be to name that variable a single underscore.
    Just because it's not required it doesn't change the correctness of the program but it signals to collegues or teachers that are looking at our code too then yes it's a variable but we don't actually care about it's name because we're not using it later.
    It's just necessary to use in order to use this Loop in this case here. so just a munor inprovement or change there.

"""
for _ in range(10):
    print("sumbaba")

"""
    We could also use_
        print("meow" * 5)
"""
print("meow" * 5)
# We could get the same result by that. But the output will be like "meowmeowmeow"
print("boom\n" * 4)
# This will fix the problem
# But if we use this instead of the while/For, the reader of the code might struggle. So the usual while/for function are good.

# We just used this feature because we wanted to show that this is a feature of python that some languages do not have.

# Printing 'meow' a variable times.
# We are now meowing some variable number of times.

# We are now going to take input from the user and then we are going to print meow that many times.
# We are not doing math here we're just meowing that many times the user gave us. So, we have to be taking a positive value.

# How can we insist on that?

n = int(input("What's n? "))
if n < 0:
    n = int(input("What's n? "))
    if n < 0:
        n = int(input("What's n? "))

# We can't do this all day unless the users still gives us nagetive numbers. We have to do something else.
# We could make a loop

# When we want to get user input that matches a certain expectation we have that it has to all positive or nagetive or something like that, then we have to use while True and create an infinite loop.

while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break
"""
    Here what did was create a loop and here we took an input then the program looked if the input was less then 0.
    If it was then the program continued and again it asked the user what is the input. Then it'll go again and again.
    If we get the the positive value than we are going to get out of the loop by typing the break.

"""
# We could also use something like that instead of using the continue function_

while True:
    n = int(input("What's n? "))
    if n >= 0:
        break

for _ in range(n):
    print("meow")



def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("How many times you want me to meow? "))
        if n > 0:
            return n
# Here we could just use return. But we could just make it perfect.
"""
    Here we could just use 'return n' but then we didn't get out of the loop, because we didn't type break.
    So it's actually inside the loop.

    If we want to use both of then what we have to do is_
    def get_number():
    while True:
        n = int(input("How many times you want me to meow? "))
        if n > 0:
            break
    return n

    Here we broke the loop but still we returned the n,
    it's still inside the function. It has to be inside the function.

"""
def meow(n):
    for _ in range(n):
        print("meow")

main()

# Let's get back to Hogwarts school
# Let's do list again

# We are going to make a list called students

students = ["Hermione", "Harry", "Ron"]
# We have to use ' "" ' in this because these are strings.

print(students)
# But this time we don't want to print out all of the things on the list.
# What if wqe want to type just a part of the list.
"""
    Let's say we want to print Harry first then Ron then Hermione, or if we want to print just Harry.
    Which I don't want to print Hermione Harry Ron all together, we just want to express more precisely which value do I want.
    And the way we use this in Python is we use square brackets in other way.

    If we have a variable in this case called students and we want to go inside of the variable and get a specific value that is to say we want to index into the list,
    We use square brackets this way using numbers inside of the square brackets

    In python the first item in a list is always at location zero and second item is one third is second and so on.
    We can say that these lists in python are always zero indexed.

"""
print(students[2])


print(students[2] , end=" ")
print(students[1] )

# if we want to create a new line between them then we have to use it like this
print(students[2] , end="\n")
print(students[1] , end="")


# Introduction to for loop

students = ["Hermione", "Harry", "Ron"]
print(students)

# If we do that than the output will be_ ["Hermione", "Harry", "Ron"]
"""
    But we want the output to be like_
    Hermione
    Harry
    Ron

    If we want that then we have to to it like_
        print(students[0])
        print(students[1])
        print(students[2])

    But then the it'll be really hard to do it manually.

"""
# Here we are introducing a new function called 'for'

for student in students:
    print(student)
"""
    The for loop in Python is a powerful control flow statement that allows you to iterate over elements in a sequence (like a list, tuple, or string) or any iterable object. It simplifies the process of performing repetitive tasks, such as printing elements in a list, without the need to write the code manually for each item in the sequence.

In your example, the for loop is used to iterate over the students list and print each student's name one by one. Here's how the loop works:

The loop starts with the keyword for, followed by a variable name (student in this case), the keyword in, and then the iterable object (students in this case). The variable student takes on the value of each element in the students list during each iteration of the loop.

The loop then executes the indented block of code below it, which simply prints the value of the student variable in each iteration. As a result, it will print each student's name on a separate line:
"""
# We said before that we could use '_', but we can't use it now. Because we are using the variable right now.




students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(students[i])

"""
    Now that we have introduced a new function called len(). Let's define it.

    The len() function is used to find out how many items are in a collection like a list, string, or dictionary. It tells you the length of the collection.

    For example1_
        text = "Hello"
        print(len(text))
    output_
        5
    For example2_
        numbers = [1, 2, 3, 4, 5]
        print(len(numbers))
    output_
        5
    For example3_
        grades = {"John": 85, "Alice": 92, "Bob": 78}
        print(len(grades))
    output_
        3

    In each example, the len() function tells you the number of items in the given collection.

"""
# Now we are using it in the loop
# Here the len(students) determines the number of items in the students list.
# Then we are puting the len(students) into the range function. Then it printed the list as usual.

"""
    Here, you use a for loop to go through the elements of the students list. range(len(students)) generates a sequence of numbers from 0 to one less than the length of the students list.

    len(students) returns the length of the students list, which is 3 in this case. So, range(len(students)) is equivalent to range(3), which generates the sequence [0, 1, 2].

    In the for loop, the variable i takes on each value from the sequence [0, 1, 2] one by one during each iteration of the loop.

    Inside the loop, students[i] is used to access the elements of the students list using the index i. Since i takes on the values [0, 1, 2], it will access the elements "Hermione", "Harry", and "Ron" respectively.

    The loop then executes the print(students[i]) statement for each iteration, which prints the name of each student on a separate line.
    This code achieves the same result as the simpler for student in students: loop that we discussed earlier. However, using range(len(students)) is less common and less Pythonic in this specific scenario. It's generally preferred to directly use the more readable and straightforward for student in students: loop to iterate over elements in a list.

"""

# So, we could also print it like this_
students = ["Hermione", "Harry", "Ron"]
for i in [0,1,3]:
    print(students[i])
# Inside the loop, students[i] is used to access the elements of the students list using the index i. So, it prints the names "Hermione", "Harry", and "Ron" one by one. also in that order.

# Let's print out not just names of students but rather let's print i first and then the student at location i.
# So two things. We know that print can take two arguements.
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i , students[i])

# Now we see that Hermione is the top student and she is in the zeroth place and that's a little weird. We want the rank to be like 1,2,3
# So we just have to do 'i + 1'

"""
    As I was writing the notes I faced a new problem. I wanted the output to be like_
0 Hermione
1 Harry
2 Ron
1 Hermione
2 Harry
3 Ron

    But as we coded the following_
    students = ["Hermione", "Harry", "Ron"]
    for i in range(len(students)):
    print(i , students[i])
    print(i + 1, students[i])

    We got the following result_
    0 Hermione
    1 Hermione
    1 Harry
    2 Harry
    2 Ron
    3 Ron

    What is the problem then?
    Explanation:
In the code above, the for loop iterates over the indices [0, 1, 2] generated by range(len(students)).

During each iteration, the print statements are executed twice:

print(i, students[i]): This prints the current index i and the corresponding student's name from the students list.

print(i + 1, students[i]): This prints the current index i + 1 and the same student's name again.

You need to modify the loop and the print statements like this:


"""
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i, students[i])
for i in range(len(students)):
    print(i + 1, students[i])

"""
student = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
"""
"""
    Here we want to make a table kind output where the students will be showed along with the houses.

"""
# We are now appointing the values of the names as the names of their houses.

students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}
# We can write it in multiple lines along with the brackets if the ususal code looks too long.

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

for student in students:
    print(student, students[student], sep=", ")
# We added the comma by adding separator function sep=", "
#Inside the loop, you use students[student] to access the value (house name) associated with the current student's name. For example, when student is "Hermione", students[student] will be "Gryffindor".

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

for _ in range(3):
    print("#")

# But we could also use it in a different way
def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")

main()

"""
    Here we are first_
        1. Defining a main function. Here we are calling a new function "print_column" and it'll be used three times.
        2. Then we are defining the "print_column". Then we are typing "for _ in range(height):" and earliar we typed "print_column(3)".
            So right here it'll be programmed "height = 3"
        3. And then we made a for loop using range function. And thus It'll be printed # 3 times.
        4. At last we called the main function.

"""
def main():
    print_column(3)


def print_column(height):
    print("#\n" * height, end="")

main()
# We could also use it like that.

"""
    What we did here is_
        instead of creating a new function we used 'print("#\n" * height, end="")'.
        Because height = 3, so '#\n" * height, end=""' means it'll multiplied by 3 and give the output on that order.

"""

def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main( )

# Till now we were coding to make the output one dimensional. But what if we want to make the output two dimensional.
# Like it'll have both length and width.

def main():
    print_square(3)

def print_square(size):
    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end=" ")
        print(end="\n")
            # We can also use only 'end="\n"'.  Both indicates a new line
main()

"""
    Inside the print_square() function, there are two nested loops that work together to print the square.
    The outer loop, for i in range(size):, iterates over each row of the square based on the given size.

    The inner loop, for j in range(size):, iterates over each brick within the current row.

    Inside the inner loop, the code prints a single brick using the print("#", end="") statement.
    The end="" argument ensures that the print statements within the same row are concatenated without adding a newline character at the end.

"""
"""
    How the program works_
        1. As usual, 'size' = 3.
        2. We defined the function 'print_square'.
        3. For i in range(3), the program will enter another inner loop.
        4. Then it'll print '###'. After that it'll go to the next line and also it'll be blank.
        5. Again it'll go back to the start of the loop and again print '###'.
    If we use end=" "_
        Then the output will be like_
            # # #
            # # #
            # # #

"""

# We could also use it like this.

def main():
    print_square(4)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#  " * width)

main()

# Here what actually happened is 4=size=width.
# We enabled the 'print_squar()' function. Then defined that function and on that function we made a loop.
# On that loop we enabled another 'print_row()' and then we defined that function.
# Here we printed the #.

# Introduction to error.

# Let's type 'print("Hello, world)'

# print("hello, world)

"""
    We will see the terminal shows "SyntaxError: unterminated string literal (detected at line 5)"
        Syntax error is a problem with the code that we have written. Our syntax just like English and other human languages have syntax assosiated with them and so does my code.
        It's not quite correct.
        The word 'unterminated' means that I started something but I didn't stop it or terminat it.

    So the fix here will be by typing ' " ' at the end.
    The 'SyntaxError' is entirely on us to solve. We have to to back to the program and fix it ourselves.

"""

x = int(input("x = ?"))
print(f"x is {x}")

# No matter what number we put it'll work unless we put floating number. But if we put alphabatical input then the program won't work.
# We will see "ValueError: invalid literal for int() with base 10: 'f'"

# The word "ValueError" suggests that the input is not supported the required value.
# It means we can't put alphabatical word into the int() function.

"""
    To solve this problem what we really want to do is write our code with error handling in mind.
    We want to write lines of code that not only accomplish the problems we care about but that also handle errors that might expectedly happen.
    In genaral when programming defensively assume that the users aren't going to be paying attention.
"""
# We have to try to fix as much as errors as we can. (Though not syntax error)
"""
    In python, there is a keyword called "try". There is also another keyword called 'except'.
    We can try using both keywords. It indicates that can I go and try to do something expect if something goes wrong I can do something else instead.

"""
# Now how can I go about trying to convert the user's input to an 'int' except if something goes wrong.

try:
    x = int(input("X = ?"))
    print(f"X is {x}")
except ValueError:
    print("X is not an integer. ")

"""
    Here we are telling the program to try to collect the input. If the input doesn't go with the 'int' function, then it goes to ValueError.
    If the program sees the valueError then it'll print that X is not an integer.
"""
# Now we try this_
try:
    x = int(input("X = ? "))
except ValueError:
    print("X is not a valid integer")

print(f"X is {x}")

# Now we see "NameError: name 'x' is not defined"
# Now we have a name error
"""
    NameError tends to refer to your code like you are doing something with the name of a variable that you shouldn't.
    Let's find out what is the actual problem. We are seeing 'name 'x' is not defined'. If we look futher here it's mentioning line 6.

"""
try:
    x = int(input("X = ? "))
except ValueError:
    print("X is not a valid integer")
else:
    print(f"X is {x}")

"""
How the program works_
    1. First the program tries to take the input as the requirement.
    2. If the program fails to get the requirement then the program prints "X is not an integer."
    3. If in the program nothing goes unwanted then the program skips the 'except ValueError' part.
    4. And then it goes to the 'else' part and prints 'X is "the given input". '
"""

try:
    x = int(input("X = ? "))
except ValueError:
    print("X is not a valid integer")
else:
    print(f"X is {x}")

"""
How the program works_
    1. First the program tries to take the input as the requirement.
    2. If the program fails to get the requirement then the program prints "X is not an integer."
    3. If in the program nothing goes unwanted then the program skips the 'except ValueError' part.
    4. And then it goes to the 'else' part and prints 'X is "the given input". '
"""

# Let's propose that we refine this just a little bit further as well and consider how we might improve this example a bit more.

# We are now going to make a loop by which we'll make the program keep asking the value to the user again and again until the program fulfills the requirements.

while True:
    try:
        x = int(input("X = ? "))
    except ValueError:
        print("X is not a valid integer")
    else:
        break

print(f"X is {x}")

"""
    Here we made a while true loop. Previously we used the else function to print the X.
    But here we are using it to get out of the loop. After getting out of the loop, it'll print the X.
    Till then the program will keep going.
"""

# We can use this program without using 'break'.

while True:
    try:
        x = int(input("X = ? "))
        break
    except ValueError:
        print("X is not an integer.")

print(f"X is {x}")

"""
    Here the program is trying to get the input in order to satisfy the requirements.
    If it does the program immediately breaks out of the loop. And prints the output.
    If it doesn't then it goes to the Except ValueError part and prints that it is not the integer.
"""

# WE CAN USE BOTH WAYS. Because even though we're trying to do two things now but one of which the break is not gonna fail.
# Because there is no peice of data that's gonna influece that.


# Let's make our own function and rebuilt this program.

def main():
    x = get_int()
    print(f"X is {x}")

def get_int():
    while True:
        try:
            x = int(input("X = ? "))
            break
        except ValueError:
            print("X is not an integer.")
    return x

main()

# Let's make our own function and rebuilt this program (The previous way).

def main():
    x = get_int()
    print(f"X is {x}")

def get_int():
    while True:
        try:
            x = int(input("X = ? "))
        except ValueError:
            print("X is not an integer.")
        else:
            break
    return x

main()

# But we can just use return instead of using both break and return.

def main():
    x = get_int()
    print(f"X is {x}")

def get_int():
    while True:
        try:
            x = int(input("X = ? "))
        except ValueError:
            print("X is not an integer.")
        else:
            return x

main()

"""
    We use the 'break' function to break out of the loop and we use 'return' function to return the value.
    But the 'return' function is stronger than 'break'.
    It not only breaks us out of the loop but also returns the value. So it's doing two things for once if you will.

"""

# Now we can just return X while trying.

def main():
    x = get_int()
    print(f"X is {x}")

def get_int():
    while True:
        try:
            return int(input("X = ? "))
        except ValueError:
            print("X is not an integer.")

main()

# Why are we defining a variable if we are directly using it in the next line and then never again.
"""
    That why we used directly 'return int(input("X = ? "))'
    instead of 'x = int(input("X = ? ")'
"""

"""
    Unless we are getting to input that satisfies the demands of the program, the program will keep asking the same question.
    What if we just want to skip the part of telling the user that their input is invalid.
    We'll just keep asking for the input.
    This is where the function 'pass' comes.

"""

def main():
    x = get_int()
    print(f"X is {x}")

def get_int():
    while True:
        try:
            return int(input("X = ? "))
        except ValueError:
            pass
main()


# A new way.
def main():
    x = get_int("What's x? ")
    print(f"X is {x}")

def get_int(Prompt):
    while True:
        try:
            return int(input(Prompt))
        except ValueError:
            pass
main()

# The get_int(Prompt) function is defined. This function takes a single argument, Prompt, which is a string that will be used as the input prompt for the user.

"""
How the program works_
    1. "What's x?" = prompt
    2. By coding 'return int(input(Prompt))' the value goes to the 'x' as long as it supports the demands. Otherwise it'll keep repeating.
    3. Then it prints the output.

"""
# Introduction to import.
# How do we load a module into our own program so that we can use functions in that module.
# For that we need a new keyword in python and it is import.

import random

coin = random.choice(['Heads', 'tails'])
print(coin)
"""
Here's a breakdown of the code:

import random: This line imports the random module, which provides various functions for generating random values.

coin = random.choice(['Heads', 'Tails']): This line uses the random.choice() function to randomly select an element from the list ['Heads', 'Tails']. This simulates the flipping of a coin with two possible outcomes: "Heads" or "Tails". The selected outcome is stored in the variable coin.

print(coin): This line prints the value stored in the coin variable, which represents the outcome of the coin flip (either "Heads" or "Tails").

When you run this code, it will randomly choose either "Heads" or "Tails" and print that chosen outcome. Since the random.choice() function is used, the result is not deterministic, meaning the output can be different each time you run the code. This simulates the randomness associated with flipping a real coin, where the outcome is uncertain.

"""


# Generate a random float between 0 and 1
"""
random_float = random.random(): This line calls the random.random() function, which returns a random floating-point number in the range [0.0, 1.0). The returned value is assigned to the variable random_float.

print(random_float): This line prints the value stored in the random_float variable, which is the randomly generated floating-point number.

The output of this code will be a random decimal number between 0 and just under 1. Since the upper bound (1.0) is exclusive, the generated number can be any value in the range [0.0, 1.0), but it will never actually be 1.0. Each time you run the code, you will get a different random number within this range.

"""
import random
random_float = random.random()
print(random_float)

"""
    In this example, random.uniform(1.1, 2.0) generates a random floating-point number between 1.1 (inclusive) and 2.0 (inclusive), which guarantees that the generated number is greater than 1.0.

You can adjust the range [1.1, 2.0] as needed to suit your specific requirements. Just make sure that the lower bound is greater than 1.0.

"""
import random

random_float = random.uniform(1.1, 2.0)  # Any range that starts above 1.0
print(random_float)


# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)

# Shuffle a list randomly
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
for list in my_list:
    print(list)
# If we don't want the program to show to brackets and all then we can just use the for loop.
"""
In this example, random.sample() will select 3 unique elements from the population list and print them as the random sample. Since the k parameter is set to 3, the resulting random_sample will contain 3 elements, and each element will be unique.

"""
import random

population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample_size = 3

random_sample = random.sample(population, sample_size)
print(random_sample)

# We also use it like this 'random_sample = random.sample(population, 3)'
"""
Certainly, here's a summary of the common random-related concepts and functions in Python:

random Module: The random module in Python provides functions for generating random values. It's part of the standard library and used for various randomization tasks.

random.random(): This function generates a random floating-point number in the range [0.0, 1.0). The generated value will be between 0 (inclusive) and 1 (exclusive).

random.randint(a, b): Generates a random integer between a and b, inclusive. The generated integer will be within the specified range.

random.uniform(a, b): Generates a random floating-point number between a and b. Both a and b are inclusive bounds.

random.choice(sequence): Picks a random element from the given sequence (e.g., list, tuple, string).

random.sample(population, k): Generates a list of k unique random elements from the given population.

random.shuffle(sequence): Shuffles the elements of a sequence randomly, altering the original sequence.

Seeding the Random Number Generator:

random.seed(seed): Sets the seed for the random number generator, ensuring reproducible random sequences when the same seed is used.
Cryptographically Secure Randomness:

For cryptographic applications, use the secrets module, which provides functions for generating cryptographically secure random values.
"""

import random

coin = random.choice(['Heads', 'Tails'])
print(coin)

# Could we implement this in a different way. This time we will use a new keyword. 'from'.

# Introduction to from.
"""
    From is a keyword in Python that we can use when importing functions from a module.
    But it allows us to be more specific than import alone.

    The difference between them is when we use 'import random' we are technically importing everything from the 'random' module.
    Not just the function 'random.choice' but few other functions as well.

        If we use import then we always have to call the functions out like 'random.choice', 'random.shuffle' etc.
            But don't have to do that in the 'from' keyword.

"""

# If we use 'from random import choice' and what it does effectively is it loads the functions name choice into our current namespace into the scope of the file we are working in.
# That means is that I now no longer have to spacify which choice function I mean. I can just say choice.

from random import choice

coin = choice(['Heads', 'tails']) #  I can just say choice.

print(coin)
# Sometimes it's better to just import the functions.
"""
There is not necessarily one right approch or another it depends but I think for those very reasons sometimes it's better to do what we did the first time which is only import the module.
So that it all the scopes so that we can can use them when the time comes.
"""

# IF we want to print just the output without the brackets then we have to use the for loop with it.

import random

cards = ['jack', 'queen', 'king']
random.shuffle(cards)
for card in cards:
    print(card)

# Introduction to Statistics
"""
    Python also comes with a statistics library. This functions are used for doing things more statistical in nature.
    Namely calculating means or medians or other aspects of data set that we might want to analyze.
"""
# Let's do an average of numbers.

import statistics
numbers=[100, 0, 900000]

average = statistics.mean(numbers)
print(average)
# We could also use the round function with the statistics modules or any kind of function that deals with numbers.

x = round(average)
print(f"{x:,}")
# We could also use the round function and use the comma as the indicators at the same time.

# Also instead of all that we can just type 'print(statistics.mean([100, 0, 900000]))'
print(statistics.mean([100, 0, 900000]))
# If we want to use the round function and the comma like before and not create the variables then the code will be like this_

print(f"{round(statistics.mean([100, 0, 900000])):,}")
# But this code would be too difficult to follow and understand.
# So in this case we better use this code by creating variables.

# There is new module named 'sys'.
# The sys module in Python is a built-in module that provides access to various system-specific parameters and functions.
# It provides an interface to the interpreter, allowing you to interact with the Python runtime environment and get information about the system where your Python script is running.

# let's go through each of the functions from the sys module, explaining what they do, providing examples, and showing the expected outputs.

# Introduction to sys.argv

# To use this function we can't just run this function.
# We have to go to the terminal and then we have to type 'python [file name] [input that I'll give]'
# Because we have to the input to the program before it starts.


# Introduction to the 'argv' function.
"""
This is a list in Python that contains the command-line arguments passed to a script when it's executed from the command line.
The first element (sys.argv[0]) is the name of the script itself. As we know the counting starts from 0 in python.
And our input goes with [1]
"""
import sys

print("Hello, my name is", sys.argv[1])
# By sys.argv[1] we are actually calling our first input. By [2], the second and so on and so on.

import sys

print("Number of command-line arguments:", len(sys.argv))
print("Script name:", sys.argv[0])
if len(sys.argv) > 1:
    print("First argument:", sys.argv[1])

print("My full name is", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
"""
    Here if we put 2 words as input then the 'Number of command-line arguments' will be 3.
        Because the name the code itself also gets itself as input because we are actually calling out the code to activate.
    And then we are printing the our first input as the script name.

    After that we are scanning the number of the input with 'len' function.
        Then if it turns out to be more than one then it prints the 2nd input, our actual input as we speak.

"""
import sys

if len(sys.argv) < 2:
    print("Too few input.")
elif len(sys.argv) > 2:
    print("Too many input.")
else:
    print("My name is", sys.argv[1])



# We could also leave or exit the program as long as it doesn't fit the requirements.
# To do that introducing a new function called 'sys.exit'. It means that we are just exiting the program.

# How the function works is_
"""
    if len(sys.argv) > 2:
        sys.exit("too few arguments.")

            We are just exiting the program as the input doesn't fulfill our demands.
            And no further code will be of deployment.
"""

import sys

if len(sys.argv) < 2:
    sys.exit("Too few input.")
elif len(sys.argv) > 2:
    sys.exit("Too many input.")

print("My name is", sys.argv[1])



# We could also leave or exit the program as long as it doesn't fit the requirements.
# To do that introducing a new function called 'sys.exit'. It means that we are just exiting the program.

# How the function works is_
"""
    if len(sys.argv) > 2:
        sys.exit("too few arguments.")

            We are just exiting the program as the input doesn't fulfill our demands.
            And no further code will be of deployment.
"""
# What if we want to print the whole thing using loop.
# What sys.argv does is the store every input within it. We can say it kind of used as list.

import sys

for arg in sys.argv:
    print("My name is", arg)
# But if we use the code like this then we face a bug.
# It also prints the script name which is in this case as we speak 'practice.py'.
# So what we have  to do is we have slice the code as we speak.

# We are actually making a slice of a list and making a subset on it.

# what We have to do is_
"""
for arg in sys.argv:
    print("My name is", arg[1:])
            By [1:] it means that we are going to start at element 1 and then everything else from that.

"""
# So this equivalently slice of the 0th element of the list and it is gonna make a new list with the rest of them.
# What if we want to erase the lase name also and print the middle part.

"""
for arg in sys.argv:
    print("My name is", arg[1:-1])
        What it means is that we are cutting out the first and the last input and we are printing the middle part.

"""
import sys

for arg in sys.argv[1:-2]:
    print("My name is", arg)

# What it does is it just erases the input according to the limit we give in the 'sys.argv[1:-2]'
# If we type in 'python practice.py boom balal vom voa' then we will get 'boom' and 'balal'.
# There is a lot of functions within 'sys' module. We can get those info by chatgpt.
# Introduction to pip
"""
    There is a lot of other functions that can be used in python but they are actually not included in python.
    We have to install them manually.
     The CS50 themselves have their own module. It's known as 'cowsay'.
     It's usually used to print our input but it actually shows that a cow is saying it to us.

"""

"""
Pip is a package manager for Python that allows you to easily install and manage Python libraries (also known as packages or modules) from the Python Package Index (PyPI) and other sources.
 Pip provides several functions and commands to help you work with Python packages. Here are some commonly used pip functions and their explanations:

"""
# To install the 'cowsay' we have to go to the command line.
# We to type 'pip install [module name]'
# In this case module name = cowsay
# And then we will call out the '.cow' function. And use it as the print function.

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Happy Birthday, " + sys.argv[1])
    cowsay.cow(f"Katla says he and you gae. {sys.argv[1]}" )

# We are going to call out the 'cow' function in the package called 'cowsay' and just use it as the print function.

# We can also use it to print not just a cow but also a trex.
# We just have to code 'cowsay.trex('input')'

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex(f"Happy birthday, {sys.argv[1]}")
    cowsay.kitty("Katla says he n u roommate?")

"""
    Here what we did is we are constantly changing the output style formula but the actual printing formula stays the same.
        If we want cow then we code 'cowsay.cow()',
        trex = cowsay.trex()
        cat = cowsay.kitty()
"""

# Now that we know how to install the no modules. Then let's install some new modules.
"""
API stands for Application Programming Interface.
 It is a set of rules and protocols that allows different software applications to communicate with each other.
 APIs define the methods and data formats that applications can use to request and exchange information.
 Here are some key points to understand about APIs:
"""
# API is an application programming interface. But often API is refer to third-party services that we write code that talk to.
"""
How this works is_
    We write code that pretends to be a browser which connects to that third party API on a server.
    Then it downloads the data that we can incorporate into our own program.
"""
# To use it we have to use a new package/module. It is really popular package that we can install via pip called 'requests'.
# The 'request' library allows us to make web request using python code essentially as though we are a browser ourselves.
#  We are gonna us URL that starts with 'http'/'https'. Let's start.

# Let's try a URL 'https://itunes.apple.com/search?entity=song&limit=<LIMIT>

# If we run this url on the browser we actually end up with a text file on the download section on our mac.
# If we enter the text file then wew see a lot of text. Which will look a bit criptic but it actually follows a pattern. \

"""
Those are actually a source code or something like that. Those are a text format known as 'JSON'
    'Javascript object notation.'
    It is related to a new language called javascript.
But JSON itself is nowadays used as a language agnostic format for exchanging data between computers.
    So we don't have to  use javascript, we can use python or any other language to read JSON or write it as well.

"""
import requests
import sys
import json

if len(sys.argv) != 3:
    sys.exit("Input not valid.")

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={sys.argv[2]}&term=" + sys.argv[1])

o = response.json()
print(f"Here is a list of {sys.argv[2]} songs of {sys.argv[1]}_")
for result in o["results"]:
    print(result["trackName"])

# what we did here is we are calling the 'get' function to get the information from the server.
# And then we are putting the input into the response variable and then printing it with the 'json' format.
# That is why we called out '.json'
"""
o appears to be a dictionary that contains a key named "results." This key likely maps to a list of dictionaries, with each dictionary representing information about a track.

The for loop iterates through each element (result) in the list associated with the "results" key.

Inside the loop, result["trackName"] accesses the value associated with the key "trackName" in the current dictionary (result), which presumably contains the name of a track.

print(result["trackName"]) then prints the track name to the console for each iteration of the loop.
"""

"""
    What happens is the whole response thing is a list of a lot of list.
        So we are first selecting the list in the response that contains the result.
        And then we are printing the list into the 'result' and printing the key that contains the trackNames.
    Summery_
    1. Entering o
    2. Going to 'results'
    3. Going to 'trackName'
    4. printing the objects that stays in 'trackname'

"""
# We have to be extra careful with the key names.
# Creating our own module like 'random', 'sys', 'json', 'request'.
# We are now creating another file and we are going to create out modules there.
# We are going to import the module from there.

# We are now creating a new function called 'saying.py'.

import sys

from saying import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

# We are now facing a weird kind of error.
"""
    On that file_
    the code is like_
        def main():
            hello("world")
            goodbye("world")

        def hello(name):
            print(f"Hello, {name}. ")

        def goodbye(name):
            print(f"Goodbye, {name}. ")

        main()
        then the output will be_
            input_python practice.py tamjid
                Hello, world.
                Goodbye, world.
                Hello, tamjid.

    We are seeing hello world and goodbye world and then we are seeing hello tamjid.
    But what we actually wanted is just 'hello, tamjid'.

    So we can deffinatly say that it's just not the way that we do it.
"""
# It's not right to call out main at the end after all.
# Even if we are importing a file or just a function from the file.
"""
    If we say 'from saying import hello' we are actually saying python to go find that module saying.py.
    Read it from top to bottom and left to right and import the hello function specifically.
    And at the end the 'call main', main gets called no matter what.
"""
# To solve it we have to do the following_
"""
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}. ")

def goodbye(name):
    print(f"Goodbye, {name}. ")

if __name__ == "__main__":
    main()
 # There is 2 underscores. We may find it hard to see in vs code
# As it turns out this '__name__' variable is a special symbol in python.
# It makes python to go to the target that we want it to go.

When you run a Python script directly (e.g., by typing python script.py in the command line), the __name__ variable is set to "__main__".

When a Python script is imported as a module into another script, the __name__ variable is set to the name of the script (without the ".py" extension).

So, you can use if __name__ == "__main__": in your script to specify what code should run only when the script is the main program, and not when it's imported as a module.
 This helps keep your code organized and separate the parts meant for execution and parts meant for reuse in other scripts.

"""
# Now it'll run perfectly
# Let's go to the calculator again

def main():
    x = int(input("x = ? "))
    print("x squared is", square(x))

def square(n):
    return n + n

if __name__ == "__main__":
    main()

# We are now creating a new python file in another file which has only one perpose that is just to check a few functions of this main file.
"""
This is what we are going to code on that file

from practice import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()
# We made a bug on the main file to make sure that the test file works.

def square(n):
    return n + n
     we coded n + n instead of n*n on perpose.


This code ensures that the main() function is only called when you run the script directly (i.e., when it's the main program),
 not when it's imported as a module into another script.

"""

# But we can see that we've written more code on the file where we are going to test than the original file.

# The fewer lines we write the greater code that we create
# Let's go to the calculator again

def main():
    x = int(input("x = ? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()

# We are now creating a new python file in another file which has only one perpose that is just to check a few functions of this main file.
"""
This is what we are going to code on that file

from practice import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()
# We made a bug on the main file to make sure that the test file works.

def square(n):
    return n + n
     we coded n + n instead of n*n on perpose.


This code ensures that the main() function is only called when you run the script directly (i.e., when it's the main program),
 not when it's imported as a module into another script.

"""

# But we can see that we've written more code on the file where we are going to test than the original file.

# The fewer lines we write the greater code that we create
# What if we have to run 2 test may be 5 or 7 or no matter how many. If we use the code like this then the code would be tremendously ling and hard to understand.

# There is another way of using this. Introducing another keyword called 'assert'.

"""
from practice import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
if __name__ == "__main__":
    main()
# There we, we are seeing nothing at the terminal and we are seeing a new error.
# It's assertion error. If we look closely then we'll see that the error is at the 8th line.

# If we use assert then we'll just see 'assertion erron' and nothing else. So we can say that it's not that user friendly
"""
"""
from practice import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
if __name__ == "__main__":
    main()
# We have try and except to make the program a bit user friendly.
# And now we can say that it solves the program.
"""
"""
    But what we are going to do if we have to do test more and more. We have to make a lot of lines to code on the test file then.
    And it'll be more than the original file of code.

    So why don't we create a tool that create the code and run the test on itself for us.
    Introducing a new tool called 'Pytest'.
        Pytest is a third party program that we can download and install that'll automate the testing of your code as long as we write the tests.
            Why are we using this?
                We are using this because we don't have to write that much code as before. And they do rest of them automatically for us.
"""
# We are proposing that we look at pytest today which is actually a little bit simpler than the unit testing Frameworks that come with python itself.
# And what is unit testing?
"""
Unit testing_
    It's a formal way of describing testing individual units of your program. And what are the unit? They typically functions.
        So we can say unit tests are actually tests for functions that you have written.
"""
# We are going to install pytest by "pip install pytest"
"""
from practice import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
"""
# To enable this we have to go to the command line and type "python -m pytest D:\test_calc.py"
"""
    1. It means first we are enabling the python.
    2. And then we are directing it to pytest by '-m'.
    3. And then we are directing the file location to pytest so that it can run.

"""
"""
    It's a bit user friendly. As we can see it's showing us_
        That we are asserting that square(3) == 9 but at the main file we are seeing 6 == 9 (Because we are using addition instead of multipication.)
    If we fix that and do the multiplication instead of addition.
"""
"""
def main():
    x = int(input("x = ? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()
"""

# Now we can see that our code passed and it works.
# Let's go to the calculator again

def main():
    x = int(input("x = ? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()

# We are now creating a new python file in another file which has only one perpose that is just to check a few functions of this main file.
"""
This is what we are going to code on that file

from practice import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()
# We made a bug on the main file to make sure that the test file works.

def square(n):
    return n + n
     we coded n + n instead of n*n on perpose.


This code ensures that the main() function is only called when you run the script directly (i.e., when it's the main program),
 not when it's imported as a module into another script.

"""

# But we can see that we've written more code on the file where we are going to test than the original file.

# The fewer lines we write the greater code that we create
# What if we have to run 2 test may be 5 or 7 or no matter how many. If we use the code like this then the code would be tremendously ling and hard to understand.

# There is another way of using this. Introducing another keyword called 'assert'.

"""
from practice import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
if __name__ == "__main__":
    main()
# There we, we are seeing nothing at the terminal and we are seeing a new error.
# It's assertion error. If we look closely then we'll see that the error is at the 8th line.

# If we use assert then we'll just see 'assertion erron' and nothing else. So we can say that it's not that user friendly
"""
"""
from practice import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
if __name__ == "__main__":
    main()
# We have try and except to make the program a bit user friendly.
# And now we can say that it solves the program.
"""
"""
    But what we are going to do if we have to do test more and more. We have to make a lot of lines to code on the test file then.
    And it'll be more than the original file of code.

    So why don't we create a tool that create the code and run the test on itself for us.
    Introducing a new tool called 'Pytest'.
        Pytest is a third party program that we can download and install that'll automate the testing of your code as long as we write the tests.
            Why are we using this?
                We are using this because we don't have to write that much code as before. And they do rest of them automatically for us.
"""
# We are proposing that we look at pytest today which is actually a little bit simpler than the unit testing Frameworks that come with python itself.
# And what is unit testing?
"""
Unit testing_
    It's a formal way of describing testing individual units of your program. And what are the unit? They typically functions.
        So we can say unit tests are actually tests for functions that you have written.
"""
# We are going to install pytest by "pip install pytest"
"""
from practice import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
"""
# To enable this we have to go to the command line and type "python -m pytest D:\test_calc.py"
"""
    1. It means first we are enabling the python.
    2. And then we are directing it to pytest by '-m'.
    3. And then we are directing the file location to pytest so that it can run.

"""
"""
    It's a bit user friendly. As we can see it's showing us_
        That we are asserting that square(3) == 9 but at the main file we are seeing 6 == 9 (Because we are using addition instead of multipication.)
    If we fix that and do the multiplication instead of addition.
"""
"""
def main():
    x = int(input("x = ? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()
"""

# Now we can see that our code passed and it works.
"""
from practice import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
def test_nagative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0

# Now at first we see 'FF.' it means first 2 programs failed and the last one passed.
# If we fix the problem again then we'll see '...'. It means all 3 passed.
# What the user gives str instead of an integer num?
# We have to test it too .
"""
# We can see if we run the program without solving the program and if we give an input which is str but not integer, then we can see the error TypeError.

# As matter of fact we can find a function of pytest.
# So we are now going to import pytest.

"""
from practice import square
import pytest


def test_positive():
    assert square(2) == 4
    assert square(3) == 9
def test_nagative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0

# Now at first we see 'FF.' it means first 2 programs failed and the last one passed.
# If we fix the problem again then we'll see '...'. It means all 3 passed.
# What the user gives str instead of an integer num?
# We have to test it too .

# We can see if we run the program without solving the program and if we give an input which is str but not integer, then we can see the error TypeError.

# As matter of fact we can find a function of pytest.
# So we are now going to import pytest.
# The function in that library called 'raises' that allows me to express that I can expect an exception to be raised.
def test_str():
    with pytest.raises(TypeError):
        square("cat")
# We have to use 'with' in this case.
# Now we can see that all 4 now are successful.

"""

# Let's create our very first function in a different way.

def main():
    name = input("What's your name? ")
    x = hello(name)
    print(x)

def hello(to="world"):
    return f"Hello, {to}"    # We are using it instead of 'print("Hello,", to)'

if __name__=="__main__":
    main()

"""
    What happened was we returned the value to hello function.
    But it can't print it by just calling it. We need to print it so we placed it in a variable.
        So we printed x as the variable.
        We could also just use 'print(hello(name))'
"""
# We are creating a new file which will test the file. It'll be called 'test_hello.py'

"""
from practice import hello

def test_default():
    assert hello() == "Hello, world"

def test_argument():
    assert hello("David") == "Hello, David"

"""

names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

# Here we first created an empty list and then we are now taking input for a significant time.
# And then we are giving input into the list. By a new function called 'append'.
"""
    {list name}.append(variable)
        What it does is, it takes the input into the the lists
"""
# We could also use it like this_
names = []

for _ in range(3):
    names.append(input("What's your name? "))

# Let's sort them alphabatically. There is litrally a function called 'sorted'.
names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"Hello, {name}")

# What it does is, it sort the names alphabatically.

# But if we run this program again all of the names are lost. So we have to re-input the same way again and again.

# So wouldn't it be nice to save this information on a file.

# That's where 'file i o' comes in.
# They are a way of storing information persistently.

# In python there is this function called open whose perpose is to do just that. Open a file.
"""
    To open it up programmatically so that we the programmer can read information from it or write information to it.

"""

# The open's documentation is here _ docs.python.org/3/library/functions.html#open

# Here is how we use it.

name = input("What's your name? ")

# open("names.txt")

 # Just because the file is gonna be text so we are naming the file as '.txt'

# But I am also going to tell the function that I am going to write on this file.

# So as a second argument to ope it I am gonna type _

file = open("names.txt", "w")

# By "w", it means that we are gonna write on the file.

# 'file' is a variable linking to the actual opened file.

file.write(name)
# It allows me to write the input from the user from the file
file.close()
# It allows me to save and close the file.

"""
If we run this program than we'll give the input and then we'll give the input.
Then we'll see nothing. What happened then?
It actually saved the name.
    Then we'll just go to the command line and type "code names.txt".
        It just opened a file and here it is. Here we can see the input on that file.

"""
# But if we rerun the file and give a new input then we'll see that the previous file was deleted and the latest input is now in existence.

# What's happenning is we are actually overwriting the fle each time.


# Let's remove the 'names.txt' file.
# Type in the command line the following "rm names.txt"

"""
    The problem is actually at the 'w' part.
        We have to append the file, not just write it.
            So we have to code it like this_
                    file = open("names.txt", "a")
"""
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()
# Now it fixes the problem but it doesn't look idle
# We are gonna have to keep creating a new line after every input.

name = (input("What's your name? "))


file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()


# We don't have to close the function manually with code.
# We can make it do so automatically.
# We are gonna have to keep creating a new line after every input.

name = (input("What's your name? "))


with open("names.txt", "a") as file:
    file.write(f"{name}\n")
# Why are we doing this?    It's just the way of activating the process.

 # What if we just want to read the file and not write it.
# I mean we want to read the loaded file.

# We are now using "r" instead of "a". as read.

with open("names.txt", "r") as file:
    Lines = file.readlines()

for line in Lines:
    print("Hello", line)

# But we can see a huge gap. Because the print already add a new line in them.

# We can just use ' end="" '. But we can introduce a new thing.


with open("names.txt", "r") as file:
    Lines = file.readlines()

for line in Lines:
    print("Hello", line.rstrip())
# ".rstip()" does the same thing as 'end=""'
# looks like the problem is solved.

# What if we can just get the same output with less lines of code.

with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())

# We are now sorting them alphabatically and also cutting out the extra gaps.
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello,{name}")

# We can also do it in a different way and less lines of code.

with open("names.txt") as file:
    for line in sorted(file):
        print("Hello,", line.rstrip() )

# But let's we want to think about upper case or lower case and then sort out each item.
# If our goal is to sort them not in the alphabatical order which is the default.
# Let's say may be reverse alphabetical orders.
"""
 Our documentation is out friend here.
    docs.python.org/3/library/functions.html#sorted

    sorted(iterable,/,*, key=None, reverse=False)

        We'll see that the 'sorted' functions takes an argument generally known as 'iterable'.
        It means that we can iterate over it.
"""
# Let's say that we can see that 'reverse=False'.
"""
    So we can say that 'reverse = False'. It's by default. So we can say that that is the reason why sort fixes everything by default alphabatically at forward.
    If we can make it True . It might work.

"""
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip().title())

for name in sorted(names, reverse=True):
    print(f"Hello,{name}")

# Looks like it worked perfect.

# Let's say we want the students other information like name and their house.
# Let's create a new file called 'names.csv'. CSV stands for 'comma separated values'
# code names.csv in the command line.


with open("student.csv") as file:
    for line in sorted(file):
        row = line.rstrip().title().split(",")
        print(f"{row[0]} is in {row[1]}")

"""
    What happpened we saved the names and houses with a comma.
    We then sorted the file and then made a row variable which stores the striped and sorted file.
    We used a new function called split(",") it means that we are spliting the file according to the comma.
    In this case it is divided into two parts. Then we printed the rows as inputs.
    If there was 2 commas, then it'll be divided into 3 parts.
    Here is an example_
"""
with open("student.csv") as file:
    for line in sorted(file):
        row = line.rstrip().title().split(",")
        print(f"{row[0]} is in {row[1]} roll {row[2]}")

# We don't necessarily have to use it like {row[1]} in fact we don't have to make them go into only one variable necessarily.
# We can just list them out like this_
# name, house, roll = line.rstrip().title().split(",")

with open("student.csv") as file:
    for line in sorted(file):
        name, house, roll = line.rstrip().title().split(",")          # Amount of the variables has to be the same as the rows.
        print(f"{name} is in {house} roll {roll}")

"""
    What happpened we saved the names and houses with a comma.
    We then sorted the file and then made a row variable which stores the striped and sorted file.
    We used a new function called split(",") it means that we are spliting the file according to the comma.
    In this case it is divided into two parts. Then we printed the rows as inputs.
    If there was 2 commas, then it'll be divided into 3 parts.
    Here is an example_
"""
with open("student.csv") as file:
    for line in sorted(file):
        row = line.rstrip().title().split(",")
        print(f"{row[0]} is in {row[1]} roll {row[2]}")

# We don't necessarily have to use it like {row[1]} in fact we don't have to make them go into only one variable necessarily.
# We can just list them out like this_
# name, house, roll = line.rstrip().title().split(",")

with open("student.csv") as file:
    for line in sorted(file):
        name, house, roll = line.rstrip().title().split(",")          # Amount of the variables has to be the same as the rows.
        print(f"{name} is in {house} roll {roll}")

# Let's say we want the students other information like name and their house.
# Let's create a new file called 'names.csv'. CSV stands for 'comma separated values'
# code names.csv in the command line.


with open("student.csv") as file:
    for line in sorted(file):
        row = line.rstrip().title().split(",")
        print(f"{row[0]} is in {row[1]}")

students = []

with open("student.csv") as file:
    for line in sorted(file):
        name, house, roll = line.rstrip().split(",")
        students.append(f"{name} is in {house} and roll {roll}")

for student in students:
    print(student)

# But if we do it this way though we can get the required code but the code is not that readable.
students = []

with open("student.csv") as file:
    for line in sorted(file):
        name, house, roll = line.rstrip().split(",")
        student = {}                     # We are creating an empty dictionary and to do so we use '{}'
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

"""
    What happened here is_
        1. student["name"] = name; Here student['name'] is where is saved the name from the line.
        2. student["house"] = house; Here student['house'] is where is saved the house from the line.
        3. Then we appending them into the students list.
"""
# We could do the same staff in one line too.
students = []

with open("student.csv") as file:
    for line in sorted(file):
        name, house, roll = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

students = []

with open("student.csv") as file:
    for line in sorted(file):
        name, house, roll = line.rstrip().title().split(",")
        student = {"name": name, "house": house, "roll": roll}
        students.append(student)

def get_name(student):
    return student["name"]
# The perpose of this function is to just return the 'name' of the student.
for student in sorted(students, key=get_name, reverse=False):
    print(f"{student['name']} is in {student['house']} and roll {student['roll']}")
# Then we are sorting out the list by the names alphabatically. Which is always there by deffault anyways.
print()
# We just used print to make a gap
# What if we want to sort this out by the rolls.

def get_roll(student):
    return student["roll"]

for student in sorted(students, key=get_roll, reverse=False):
    print(f"{student['name']} is in {student['house']} and roll {student['roll']}")
# Let's do it with houses.
print()

def get_houses(student):
    return student["house"]

for student in sorted(students, key=get_houses, reverse=False):
    print(f"{student['name']} is in {student['house']} and roll {student['roll']}")

# What if we don't have to define the function anymore
print()
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']} and roll {student['roll']}")
# 'key=lambda student: student["name"]'  this thing actually does the work of defining the functions.
# We just have to change the 'student['name']' part according to out demand.

"""
Let's add address of the students as follows_

Hermione,Gryffindor,1,120,jamalkhan
Harry,Gryffindor,2,leaf village
Ron,Gryffindor,3,sand village
Draco,Slytherin,4,new work
"""
students = []

with open('student.csv') as file:
    for line in file:
        name, house, roll, home = line.rstrip().title().split(",")
        student = {'name': name, 'house': house, 'roll':roll, 'home':home}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['house']}")
    print(f"He is from {student['home']}")


# If we get the  address with comma like '120,jamalkhan'
# But now we can see that there is an error. We'll see "too many values to unpack (expected 4)"

"""
There is a module called 'CSV'
    It's documentation is in the following link_
        docs.python.org/3/library/csv.html
We are now importing the module.
"""
import csv

students = []

with open("student.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({'name':name, 'home':home})

for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is from {student['home']}")
import csv

students = []

with open("student.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row['name'], "home": row['home']})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

"""
    Here we used csv.DictReader(file) instead of csv.reader(file) and then it read the file as a dictionary.
    and we created a row in reader for loop and we aligned the row which contains 'name' to the "name".
    and the "home" the same way.
        To use csv.DictReader(file), we just have to add the new Row on the Csv file as follows_
            name,home
            Hermione,"jamalkhan, chittagong"
            Harry,leaf village
            Ron,sand village
            Draco,new work
        So even if we turn it the other way then still we'll get the perfect output.
        home,name
        "jamalkhan, chittagong",Hermione
        leaf village,Harry
        sand village,Ron
        new work,Draco


"""


import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("student.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])



import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("student.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name,"home": home})







import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=images[1:], duration=200, loop=0
)
"""
Importing Libraries:

import sys: This imports the sys module, which provides access to some variables used or maintained by the Python interpreter and to functions that interact with the interpreter.
from PIL import Image: This imports the Image class from the Python Imaging Library (PIL), which is used for opening, manipulating, and saving image files.
Initialization:

images = []: This initializes an empty list named images where we will store the images that will be used to create the animated GIF.

"""
"""
Looping Through Command Line Arguments:
for arg in sys.argv[1:]:: This loop iterates over the command-line arguments passed when the script is run. sys.argv[1:] excludes the first argument, which is the script name itself.
Opening and Appending Images:
image = Image.open(arg): This opens an image file specified by the command-line argument arg and assigns it to the variable image.
images.append(image): This appends the opened image to the images list.

"""
"""
Saving the Animated GIF:
images[0].save(...): This line is trying to save an animated GIF using the first image from the list.

save_all=True: This parameter specifies that all frames (images) should be saved in the output GIF.

append_images=images[1:]: This includes all the subsequent images in the GIF.

duration=200: This sets the duration of each frame in milliseconds (200 milliseconds in this case).

loop=0: This specifies that the animation should loop indefinitely.

"costumes.gif": This is the output file name for the animated GIF.

"""
"""
The line append_images=images[1:] is used to include all images except the first one in the creation of the animated GIF.

Here's why:

images[1:] returns a sublist of images starting from the second element (index 1) to the last element. This is achieved using slicing.

In the context of creating an animated GIF, this means that all images from the second one onwards will be included in the animation.

If we used images[1] instead, it would only include the second image. This would result in a GIF with only two frames - the first frame being the base image (index 0) and the second frame being the second image (index 1).

By using images[1:], we ensure that all images provided in the command-line arguments are included in the final animated GIF, resulting in a smoother animation with multiple frames.

"""



email = input("What is yu email? ").strip

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")




email = input("What is yu email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
#----------------------------------

email = input("What is yu email? ").strip()

username, domain = email.split("@")

if username:
    print("Valid")
else:
    print("Invalid")

"""
    Here the "if username:" part means that it has to contain at least one test/number or something.
    Then it'll be valid. If we just enter the input like_"@gmail.com" then it won't work.

"""

email = input("What is yu email? ").strip()
if "@" in email and "." in email:

    username, domain = email.split("@")

    if username and "." in domain:
        print("Valid")
    else:
        print("Invalid")

else:
    print("Invalid.")

#---------------------------

# Validates email address by checking whether domain ends with .edu

email = input("What is yu email? ").strip()
if "@" in email and "." in email:

    username, domain = email.split("@")

    if username and domain.endswith(".edu"):            # Now the input has to be "tmjd@harvard.edu"
        print("Valid")
    else:
        print("Invalid")

else:
    print("Invalid.")



# Validates email address by checking whether domain ends with .edu

email = input("What's your email? ").strip()
if "@" in email and "." in email:
    username, domain = email.split("@")

    if username and domain.endswith(".edu"):
        print("Valid")
    else:
        print("Invalid")

# Validates email address by checking for @ with regex.

import re
email = input("what's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("invalid")
#_______________________________


# Adds .*
import re

email = input("What's your email? ").strip()

if re.search(".*@.*",email):
        print("valid")
else:
    print("Invalid")

# In this case if we give the input like this "tmjd@" ....without any domain, then this is going to say that it is valid...as we all know that ".*" means any character except a newline and 0 or more repetition.
# So if we don't enter anything ....still the output will say that it is valid


#__________________________
import re

email = input("What's your email? ").strip()

if re.search(".+@.+",email):
        print("valid")
else:
    print("Invalid")


# If we use "+" instead of ".".....then it works perfectly

# We could also use it without using the "+"

import re

email = input("What's your email? ").strip()

if re.search("..*@..*",email):
        print("valid")
else:
    print("Invalid")

"""
    Here the "..*" means_
        The first "." means any character.
        And the socond ".*" means zero or more other characters.

"""
# So technically we can say that ..* = .+

# What if I want the whole thing to end with ".edu".
"""
    We obviously can't use something like "re.search(".+@.+.edu",email)" because here...the dot is actually being used for a different use.
    We'll just simply use "re.search(".+@.+/.edu",email)"
    This single backslash actually solves the whole problem.

"""
# But if we just give input like this "hsntmjd@@@g.edu"...then it'll work.
# To solve this we are getiing a new function called "r".

# And we want to specify the regular expression and double quote to read it as a row string.
# We are just litarally putting an "r" at the beginning of the string.
# To indicate to python that "you should not try to interpret any backlashes in the usual way."
# We've used "f" to usually format the string and now we're using "r". To indicate a row string that I want passed in as exactly as is.

import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu",email):
        print("valid")
else:
    print("Invalid")


# Let's introduce a few more symbols as well.
"""
    ^   matches the start of the string
    $   matches the end of the string or just before the newline at the end of the string.

"""


import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$",email):
        print("Valid")
else:
    print("Invalid")


# Let's try something new.


# The new function is just [^@].

import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$",email):
        print("Valid")
else:
    print("Invalid")

"""
    []  set of characters
    [^] complementing the set

    [] - we kinda use it to make a list and to specify that if any of the characters contains on the input then the input will be valid.
        like if we use it like this [abcd] _ it means any of them would work.
    [^] - it means the whole set of the list.
        like [^@] means any of the characters except the "@".
"""


"""
    if re.search(r"^[^@]+@[^@]+\.edu$", email):: This line contains an if statement that checks a condition using a regular expression pattern.

    re.search(pattern, string) is a function provided by the re module. It searches for the first occurrence of the pattern in the string. In this case, it searches for the pattern within the email string.

    The pattern is specified as a raw string r"^[^@]+@[^@]+\.edu$":

    ^: Asserts the start of a line.
    [^@]+: Matches one or more characters that are not @.
    @: Matches the literal @ character.
    [^@]+: Matches one or more characters that are not @.
    \.: Matches a literal period .. The \ is used to escape the special meaning of . in regular expressions.
    edu: Matches the literal characters "edu".
    $: Asserts the end of a line.
    If the pattern is found in the email string, the condition is considered True, indicating that the email matches the specified pattern.
"""

# What if we want to say to program that we can get any kind of alphabets or numbers or in some cases underscores also.
# And we want to count them as valid.
"""
    We just have to use [] and list them out.
    we don't even have to type in "a-z". If we want it to accept capital letter too, the we just have to use [a-zA-Z].
        We don't have to use any kind of space or commas...or anything.
    sometimes people uses underscores too....then we just have to use [a-zA-Z_]...so what if numbers [a-zA-Z0-9_]
"""
import re

email =  input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.edu$", email):
    print("Valid")

else:
    print("Invalid")



# We could just skip the whole "[a-zA-Z0-9]" thing with a new type of keyword called "\w".
# It kinda represents a word character which is commonly known as "Alpha numeric symbol/underscore."
# So we can just use it like this_

import re

email =  input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")

else:
    print("Invalid")

"""
    \d  decimal digit
    \D  not a decimal
    \s  whitespace characters
    \S  not a whitespace character
    \w  word character...as well as numbers and the underscore
    \W  not a characters
"""
# What if we want the email to be ended with not only just '.edu' but also some other staff as well.
# Then we just have to make a list inside the research funtion.

# Then the code will be like this_


import re

email =  input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(edu|com|org|net|co)$", email):       # Here we've now made a list and now it's going to work if the input email ends with either of them.
    print("Valid")

else:
    print("Invalid")

"""
    Let's rewind the verticle bars again_
        The verticle bar means "or" and the brackets just simply group things together.
    Normally we have this syntax here_


"""
# What if we want "space" to be accepted in the email.
import re

email =  input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9 ]+@[a-zA-Z0-9 ]+\.edu$", email):           # We just have to add "space" into it.
    print("Valid")

else:
    print("Invalid")

# If our given input has some uppercase letters then the program will still take it as valid.
# But if every word of our input is capitalized then the program will be showing us that the program is invalid.
# So we can just take the whole input as lowercase by ourselves. Using the "lower()".
# By using that we just forced it all to lowercase. 


import re

email =  input("What's your email? ").strip().lower()

if re.search(r"^\w+@\w+\.(edu|com|org|net|co)$", email):       
    print("Valid")

else:
    print("Invalid")
# Or we could do this a little bit later...like this
import re

email =  input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(edu|com|org|net|co)$", email.lower()):       
    print("Valid")

else:
    print("Invalid")

# This would work too. But we could do this another way.

"""
    The 're.search' funct(ion before actually works like this as we all know_
        re.search(pattern, string)
    But it turns out this functions supports a third argument as well.
    "flags"
    
        'flags' are a configuration option typically to a function that allows us to configure it a little differently.
    
    Some of the flags that we can pass into this function are these_
        re.IGNORECASE
        re.MULTILINE
        re.DOTALL
    

    It turns out the regular expression library in python AKA re comes with a few built in variables so to speak.
    Things that we can think of as constants that have meaning to re.search and they do so as follows. 

"""
# If we pass into a flag re.ignore case, what re.search is going to do is ignore the case of the users input.
# It can be uppercase lowercase a fcombination there of, the case is point to be ignored and it'll be treated insensitively.



# What if the user didn't type in an email address as we wanted. What if they gave a whole paragraph like input instead of just an email.
# And we want to match different lines of that text.

# This is where the 're.MULTILINE' comes. Or 're.all' whereby we can configure the dot to recognize not just any character except new lines but any character + newline.

import re

email =  input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|org|net|co)$", email, re.IGNORECASE):     # We did it like that so that we can say that it's valid  
    print("Valid")

else:
    print("Invalid")







# But sometimes we can see other kinds of email addresses. Like_ "Hsntmjd@harvard.edu.org"
# We can see that there is miltiple "." and other texts.
# We have to give that kind of codes regarding to the demand by using "\w"
import re

email =  input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.\w+\.(edu|com|org|net|co)$", email.lower()):     # We did it like that so that we can say that it's valid  
    print("Valid")

else:
    print("Invalid")

# But now if we give the input with the usual email id's, then the program will say that the given email is invalid.
# So we have to make a program which accepts both of them.


# To solve the problem let's go to out very first list regarding email syntaxes.

"""
    .       any character except a newline
    *       0 or more repetition
    +       1 or more repetiion
    ?       0 or 1 repetition
    {m}     m repetitions
    {m,n}   m-n repetitions
"""

# We are now gonna use the "?  0 or 1 repetition" part.
# The "?" means zero or one repetitions which effectively means optional.
# It's either there(1) or it's not (0).


# We are just going to use parenthesis to solve the question.
# We first just grouped the "\w+\." and this now still work and it won't effect the program.
# Because we've only added parenthesis around the new part for the subdomain. But then still the output would be invalid.

# But in the parenthesis we can say that it's one big logical unit, a big group of ideas together.
# Now we add a single question mark there. like this_"(\w+\.)?"

# This will now tell our "re.search" that the whole thing in parenthesis can either be there once or be there not at all.




import re

email =  input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|org|net|co)$", email.lower()):     # We did it like that so that we can say that it's valid  
    print("Valid")

else:
    print("Invalid")
 
 # And that solves the problem.

# But we might feel that it's hard to understand the whole "re.search" function. Because it's too cryptic right now.

# Let's break it down now.


"""
    Let's break down the code:

    if: This is a conditional statement in Python. It allows you to execute a block of code only if a certain condition is true.

    re.search(pattern, string): This is a function call to the search function from the re module. It searches for a specified pattern (regular expression) within a string. In this case, it's used to search for a specific pattern in the email string.

    r"^\w+@(\w+\.)?\w+\.(edu|com|org|net|co)$": This is a regular expression pattern. Let's break it down:

    r": Indicates that this is a raw string, which allows for easier handling of backslashes in regular expressions.
    ^: Asserts the start of a line.
    \w+: Matches one or more word characters (letters, digits, or underscores). This represents the username part of an email address.
    @: Matches the literal "@" symbol.
    (\w+\.)?: This is a non-capturing group ( )?. It matches zero or one occurrence of the group. In this case, it matches an optional group that contains one or more word characters followed by a dot. This is for handling subdomains in the domain name (e.g., subdomain.example.com).
    \w+: Matches one or more word characters. This represents the main domain name part before the dot (e.g., "example" in "example.com").
    \.: Matches a literal dot (".") character.
    (edu|com|org|net|co): This is an alternation ( ) group that matches one of the specified options inside the parentheses. In this case, it matches "edu", "com", "org", "net", or "co".
    $: Asserts the end of a line.
    So, this regular expression pattern is designed to match email addresses that have a specific format: <username>@<subdomain>.<domain>.<extension>, where the domain extension can be "edu", "com", "org", "net", or "co".

    email.lower(): This converts the entire email address to lowercase. This ensures that the regular expression pattern matches regardless of the case of the email address. For example, "example@domain.com" and "Example@Domain.com" would both be considered valid.

    If the regular expression pattern matches the provided email address, the if condition is considered true, and the code block within the if statement will be executed (i.e., print("Valid")). Otherwise, if the pattern does not match, the else block will be executed (i.e., print("Invalid")).
"""

# What if we want a "." to be allowed before the "@".
# We just have to use list as before.
# Also we don't have speficially show the "Uppercase" since we are now ignoring the case of the letters.


import re

email =  input("What's your email? ").strip()

if re.search(r"^[a-z0-9\. ]+@[a-z0-9 ]+\.edu$", email, re.IGNORECASE):          
    print("Valid")

else:
    print("Invalid")

# And luckily if we use the code like this the whole problem of accepting the unique kinds of emails which contains multiple ".".

# HOW????

# Since we are making lists of the choices/demands, why don't we just do the same thing as we did for the part that stands before the "@"

# We have allowed the "." in the begining og the email. Why don't we just do the same thing after the '@' part too.
# That just solves the whole problem.

import re

email =  input("What's your email? ").strip()

if re.search(r"^[a-z0-9\. ]+@[a-z0-9\. ]+\.edu$", email, re.IGNORECASE):          
    print("Valid")

else:
    print("Invalid")

"""
    "if re.search(r"^[a-z0-9\. ]+@[a-z0-9\. ]+\.edu$", email, re.IGNORECASE):  "
    the given code means_
        [a-z0-9\. ]   we are accepting "." at the beginnig of the email.
        [a-z0-9\. ]   we are also accepting "." after "@". It doesn't matter how many "." there is..
            The main demand now is that it has to end with ".edu"
            
"""

"""
    ^[a-zA-Z0-9. !#$%&' *+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

    This the actual formula which is now used in websites to see if the given email id is valid.
    
"""
import re

email =  input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9. !#$%&' *+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email, re.IGNORECASE):          
    print("Valid")

else:
    print("Invalid")


# Let's try this function with some of our old code

name = input("What's your name? ").strip()
print(f"Hello, {name}")

# But here comes a catch.
"""
    What if we give our input as something like that "Hossain, Tamjid".
        But then the output will be like_ "Hello, Hossain, Tamjid"
    But we don't the program to do something like that.
"""
  

name = input("What's your name? ").strip()

if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"        # We are now remaking the name in a new format.
print(f"Hello, {name}")    # By that it means if the given input has comma in it then the "if" program is gonna work and it's going to override the input.

# If it doesn't has comma then it's just going to print what was just given to the progam.
"""
    The "f" function actually works to format something. 
    As we just devided the previous name into two pieces, we now have two variables.
    And then we are recreating the name variable.
        By the "name = f'{first} {last}'",
             It means that the new name string now contains the input on this format right now "Hossain Tamjid"
                But before it was like that "Hossain, Tamjid" and it didn't look good
    By doing that we are actually overriding user's input.

"""
# This code right now fixes most of our problem. But what could go wrong even with this input.

"""
    1. What if we use something like that in the input_
        Hossain, Tamjid
    Then the program is going to print "Hello, Tamjid Hossain".
        As we can see it actually rearranged my name. But it is not a big issue here.

    2. But what if my name is "Hossain Tamjid, jr"
        Then the output will be like this "Hello, jr Hossain Tamjid". Now it's a problem. It just messed up my name.
    
    3. What if we just give the input like that now_ 
        Hossain,Tamjid     (It has no spaces after the comma)
    Then we are gonna see the valueerror.
        What exactly is happening here?
            Well we've used "split(", ")"
             Here the spilt is is actually spiltting the input in respect of comma and space.
              So if the program can't find both comma and space it just cant devide the program.
              


"""


import re 

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"Hello, {name}")

"""
 Let's go through the code step by step:

    import re: This line imports the regular expressions (regex) module, re, which provides functions for working with regular expressions.

    name = input("What's your name? ").strip(): This line prompts the user to enter their name and then assigns the input to the variable name. The .strip() method is used to remove any leading or trailing spaces from the input. This ensures that there are no unwanted spaces affecting the name.

    matches = re.search(r"^(.+), (.+)$", name): This line uses a regular expression pattern to search for a specific pattern in the name string. Let's break down the pattern:

    ^: Asserts the start of a line.
    (.+): This is a capturing group ( ) that matches one or more occurrences + of any character . (except for a newline). This represents the last name.
    In the regular expression ^(.+), (.+)$, the (.+) parts are called "capturing groups". They are used to capture (or extract) specific portions of the matched text.

    , : Matches a comma and a space.
    (.+): Another capturing group that matches one or more occurrences of any character. This represents the first name.
    $: Asserts the end of a line.
    The regular expression pattern is designed to match names in the format "Last, First".

    If a match is found, re.search() returns a match object. If no match is found, it returns None. The match object is then assigned to the variable matches.

    if matches:: This checks whether a match was found. If a match was found (meaning matches is not None), the condition is considered true.

    last, first = matches.groups(): If there was a match, this line extracts the captured groups (last name and first name) from the match object.

    name = f"{first} {last}": This line reassigns the name variable with the first name and last name reversed and separated by a space.

    print(f"Hello, {name}"): Finally, this line prints a greeting message using the modified name.

    In summary, the code prompts the user for their name, expects it to be in the format "Last, First", rearranges it to "First Last", and then greets the user using the modified name. If the user enters a name in a different format, the code won't perform the rearrangement.

"""

import re

name = input("What's your name? ").strip()
match = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"

print(f"Hello, {name}")


"""
    last, first = matches.groups()
      If we do this it'll automatically allocate the "first" into to the matching group 2, because we listed it out after the 'last'.
    But in the second code, made it clear that we can control that too.
    
"""

# We could also use it another way.

import re

name = input("What's your name? ").strip().title()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")


"""
    By "if matches:
        name = matches.group(2) + " " + matches.group(1)"

    It means if the given conditions match, we are now overriding the 'name' string. And the captured groups will be divided.
    The first one is group one and the second one is second. 
        Now the new variable is_
            group 1 and 'space' then group 2.
        So It just erases the comma and solves the problem.
"""

# What if we are some kinda weird user and now we are giving the input like this_ 'hossain,      tamjid'

# Well now we are facing a new problem.
# We are now getting the output like this_ 'Hello,            Tamjid Hossain'

# What if we are giving the input like this_ 'hossain,tamjid' (with no space.)
# Now we see a new problem.
# We are now getting the input like this_'Hello, hossain,tamjid.'
    # Why is that? Because we ask for a space along with the comma at the re.search part. Here we are still looking for comma and sapce.


# We are going to solve it by doing this_

# By doing this we can solve the 'no space' problem. 

import re

name = input("What's your name? ").strip().title()
matches = re.search(r"^(.+), ?(.+)$", name)         # Here we just added a question mark which means 0 or 1.
if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")

# Now if we give the input like this_ 'hossain,tamjid', we still get the prefect result.


# What about the 'too much space' problem?
 
import re

name = input("What's your name? ").strip().title()
matches = re.search(r"^(.+), *(.+)$", name)         # Here we just added a star mark which means 0 or more.
if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")

# The given code recently solves the both problems at the same time actually.


# What if we want to do the 'matches' part on just one line and move on or something like that


# Use of walrus operator.
import re

name = input("What's your name? ").strip().title()

if matches := re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")


"""
    matches :=: This is a combination of the assignment operator :=. 
    It's known as the "walrus operator," introduced in Python 3.8. 
    It assigns the result of the expression on the right to the variable on the left.
"""

# Here we actually did 2 things at once. If it was java/c/ c++ then we had to do a lot of work with the perenthesis.
# But we don't have to do any of that with python.


# Here we not only assigned the return value of 're.search' to a variable called 'matches'..
# We want to subsequently ask a boolean question "Is this effectively true or not? "
# That's what we were doing at the previous code.

"""
    Then we were getting back the return value and assigning it to matches and then we were asking the question.

"""

# What we did at the recent code? We just combined both of them together at the single line.

# But to do that we need a new operator.

# Introducing the ":=". It is known as the walrus operator

"""
    It is used if we want to assign something from right to left,
        And if we want to ask an if or an elif question on the same line.
"""

# It allows us to assign a value as we are doing from right to left and ask a boolean question about it

# Fun fact why is it called walrus?
    # If we look at ":=" as like landscape it kinda looks like an walrus.


# we will the original url or elon musk's twitter url. which is "https://twitter.com/elonmusk"

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "").title()
print(f"Username: {username}")

# But what if the user is a little weird and he answered like this_
"""
    URL: My URL is https://twitter.com/elonmusk
    
        Then what happens is we are gonna get the output like this_
            Hello, My URL Is Elonmusk.

    What the program did was just replaced the URL part.
    But we need to get the only "after URl part."

"""
# So, we technically just have to remove the prefix along with the url.


    # Prefix is a string or a substring that comes at the start of another. 

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/").title()
print(f"Username: {username}")

# And it solves the problem.
# But the name "Elon Musk" is showing "Elonmusk". That's another problem.


# We are now introducing a new function called 're.sub'. Here the 'sub' stands for substitution.

"""
    Here is how it works_
        re.sub(pattern, repl, string, count=0 , flag=0)
            * The pattern in this case the link.
            * The part we'll replace it with.
            * The count and the flag.


            Here 'count' means how many times we want to find and replace.
            Like do we want to do all? just one or something like that.

"""
import re
url = input("URL: ").strip()

username = re.sub("https://twitter.com/", "", url).title()
print(f"Username: {username}")
 


         

# We are now using row function to be more specific.

import re
url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url).title()
print(f"Username: {username}")

# Here the by the row function we specified_
"""
    Regular Expression: r"^(https?://)?(www\.)?twitter\.com/"
    Explanation: This pattern matches the beginning of the string (^), 
        followed by an optional http:// or https:// ((https?://)?), although we could use something like this_ http|https. But we just don't have to.
        followed by an optional www. ((www\.)?), and then twitter.com/.
    When you apply this pattern to the input 'https://twitter.com/elonmusk', it matches and removes 'https://twitter.com/', leaving 'elonmusk'.
"""

# BUT....We can see a big issue here.
# If we use the code like this_
import re
url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/$", "", url).title()
print(f"Username: {username}")

# Then the program won't work.

"""
    If we use the dollar sign here then program will just fail.
    This pattern is similar to the first one, but it has an additional $ at the end. 
    In regular expressions, $ represents the end of a line or string. 
    This means the pattern will only match URLs that end with twitter.com/.
    When you apply this pattern to the input 'https://twitter.com/elonmusk', it doesn't match because the URL doesn't end with twitter.com/. Therefore, the replacement doesn't happen, and the original URL is returned.    

"""

# But there still remains arguable at least one problem with this solution in that.
# Even though we are calling 're.sub' to substitute the URL with nothing by using ' "" '

# And then we are blindly hoping that it'll work.

"""
    But what if the user instead of giving the URL of twitter, he gives something else.
    What if they do something like that_ https://www.google.com/   (completely unrelated)
        Then if we run this then we see that it just prints exactly that.

        We have re.sub to get rid of something we don't want there. But to solve the problem why don't we just go back to re.search.

"""

import re 

url = input("URL: ").strip().title()


if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
# Now although it solves the invalid link issue but now it is showing 'Username: None' when we give a valid URL.
# Also if we use the 'www.' then we'll see the 'www.' at the 'Username:' part.

"""
    What happened here is the subdomain is optional. 
    And to make it optional we needed to use parentheses. And then we said zero or one.
        That means we are unintentionally by design capturing the 'www.' or nothing if it wasn't there before.
    But we have a second match over the (.+). As we have the second set of parentheses.

        So if we just change the matches.group(1) into matches.group(2). 
        And now it works.

"""
# So although we have solved the issue. Now we are facing a new problem.
# If we use brackets then we are automatically capturing it.
"""
    a|b     either a or b
    (..)    a group
    (?:..)   non-capturing version

    If we want to use parentheses logically because we need to but you don't want to bother capturing the result.

"""

"""
    As we see on the previous code, I do need to surround the 'www.' with parentheses but we don't want to capture it.
    As we did the '?' it means if exists it'll work and if it doesn't it doesn't hurt. But problem was it just captures the thing.
    So we are now using (?:...) in this part.
""" 

import re 

url = input("URL: ").strip().title()


if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")

# Now it works too.
# But what if we want to end it with 'com'/'org'.

import re 

url = input("URL: ").strip().title()


if matches := re.search(r"^https?://(?:www\.)?twitter\.(.+)/(.+)$", url, re.IGNORECASE):
    if matches.group(1).lower() == "com" or matches.group(1).lower() == "org":
        print(f"Username: {matches.group(2)}")

# Here we used the 'https?://(?:www\.)?twitter\.(.+)/(.+)$' the first group is matched the the word 'com' then the programs continues.

# But we can just use it the easy way.

import re 

url = input("URL: ").strip().title()


if matches := re.search(r"^https?://(?:www\.)?twitter\.(?:com|org)/(.+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
# And if we do it like this we won't have to capture them 


# What if we want to just use it the usual way '[a-z0-9_]'. But we now want to accept the URL even if it ends with some other symbols

import re 

url = input("URL: ").strip().title()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")


"""
    +: This is a quantifier that means "one or more". 
    It specifies that the preceding character or group (in this case, the character class [a-z0-9_]) must occur one or more times.
"""

# Welcome to object oriented programming
"""
    Object-Oriented Programming (OOP) is a programming paradigm that is based on the concept of "objects", which can contain data and code to manipulate that data.
    It's a way of organizing code to model real-world entities or abstract concepts
"""

name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")


# We are now going to try the same thing with the functions.

def main():
    name = get_name()
    house = get_house()
    print(f"{name} is from {house}")


def get_name():
    name = input("Name: ")
    return name 

def get_house():
    house = input("House: ")
    return house 
main()

# But here we don't need to get the house/name variable and then returned it immediately. And then the use of those variables are none.

# We can do the same thing without using the variables. We can just return the gotten input.

def main():
    name = get_name()
    house = get_house()
    print(f"{name} is from {house}")


def get_name():
    return input("Name: ")
      

def get_house():
    return input("House: ")

if __name__=="__main__":
    main()

# But now we want to define a function called 'get_student' and let 'get_student' do all of this work for us.

# Theoretically it's gonna call get_name, get_house.

# We are now trying to make just one function and then just using variables.


def main():
    name, house = get_student()         # Here we took as the input. And the firstly returned string went to the 'name' and the other one into the 'house' variable.
    print(f"{name} is from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house              # Here we did something new which is, we returned 2 variables into to defined function.

if __name__ =="__main__":
    main()
# Although we used the the same variable in the defining the 'get_student' part as well as the main() part.
# It just won't hurt to do so and it is more readable and understandable this way.


# Introduction to tuple.
"""
    A tuple is an ordered, immutable collection of elements. 
    In Python,a tuple is created by enclosing a comma-separated sequence of values within parentheses
"""

# A list we've seen before which is a data structure in python that we can change the values of.
# But if we have no intention of changing the values of variables and we want to return effectively multiple values.
# We don't even have to return it as a list. We can just return it as a tuple instead just by using a comma.


# This is the exact thing what we did before.
"""
    We didn't just returned the two value per se whenever we use a comma in this way on line 9
    we are actually returning one value which is a 'tuple'.
        And inside of that tuple now are two values.
        It is similiar spirit of returning one list with two things. The comma here tells python that we indeed want to return a tuple.

"""
# But there is more explicit syntax that we can use instead we can actually more verbosely put explicit parentheses around the values of this tuple.
# Just to make more clear to the reader that this isn't two values per se.. But this one value with two things inside of it
# And then we can just use one variable at the defining the main() function.

def main():
    student = get_student()         
    print(f"{student[0]} is from {student[1]}")     # Here the student[0] = name, student[1] = house. 

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)              

if __name__ =="__main__":
    main()


# What if we want to check the input with some issue and if it matches then we want to change the other input part the some especific string.

def main():
    student = get_student() 
    if student[0] == 'padma':
        student[1] = 'Ravenclaw'     # It is the especific string.
             
    print(f"{student[0]} is from {student[1]}")      

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)              

if __name__ =="__main__":
    main()


"""
    Now if we just use some random input then the program works perfectly.
        But if we use the 'padma' (the especific issue/string) then are now facing a new error.
    We are seeeing ''tuple' object does not support item assignment'. We are seeing that a typeerror has happened.
            It means we cannot change location 0 or 1 or anything inside. And that's how the tuple works. We can't change anything.

            
    So if we want to override that we have to try some other way.
        We are now going to use list to solve the problem.

"""

def main():
    student = get_student() 
    if student[0] == 'padma':
        student[1] = 'Ravenclaw'     
             
    print(f"{student[0]} is from {student[1]}")      

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]             # We have used third brackets instead of the tuple with parentheses.

if __name__ =="__main__":
    main()

# And it just solves the problem because we can override the inputs now .

# What if we want to create dict. Not list/tuple.

def main():
    student = get_student()          
    print(f"{student['name']} is from {student['house']}")      

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
if __name__ =="__main__":
    main()

# Instead of returning any variable name student which we're gonna propose doesn't need to exist anymore.
# Let's do something like that_


def main():
    student = get_student()          
    print(f"{student['name']} is from {student['house']}")      

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}       # Here we just created and returned a dictionary in one line.
if __name__ =="__main__":
    main()



# Let's bring back 'padma' again now.

def main():
    student = get_student()     
    if student["name"] == "padma":
        student["house"] = "Ravenclaw"   
    print(f"{student['name']} is from {student['house']}")      

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}      
if __name__ =="__main__":
    main()

# Python gave us some general purpose tool that's going to allow us to create our own datatypes as well and actually give them names.
# And that's terminology is called class.
"""
    In Python, a class is a blueprint for creating objects. 
    It defines a set of attributes (data members) and methods (functions) that the objects of the class will have. 
    Essentially, a class provides a template for creating objects with specific characteristics and behaviors
"""
# In short classes allow you to invent your own data type in python and give them a name.
# It is a primary feature of object oriented programming to be able to create your own objects.

class Student:
    ...

def main():
    student = get_student()          
    print(f"{student.name} is from {student.house}")      

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student       
if __name__ =="__main__":
    main()


# We could use it the other way too.

class Student:
    ...

def main():
    student = get_student()          
    print(f"{student.name} is from {student.house}")      

def get_student():
    student = Student()
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student       
if __name__ =="__main__":
    main()

# By that fundamentally we are still getting the same output in the same way.
# We just happen to be storing those return values in local variables but now we are setting the stage for more powerful features of classes.


"""
    Notice that we are deliverately passing to the Capital S student function name comma house. 
    We are passing in arguments to the function. 
    Now the student class is not going to do with those yet. 
        But now we are sort of standardizing how we are passing data into the student class and it's gonna give me the chance to error check to those inputs.
    It's going to allow me to ensure that it's a valid house that it's Gryffindor/Hufflepuff/Revenclaw/Slytherin or not just hitting enter or some random value that the user, 
        Because we are putting those staffs into the Student class, we are gonna have more control over the correctness of my data.
    
        
    Let's go to the student class where till now we just put '...' it turns out that in the context of classes there are not just attributes or instance variables we can put inside but also methods.
        Classes come with certain methods or functions inside that we can define and they just behave in a special way by nature of how python works.

"""

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()

"""
    def: This keyword is used to define a function in Python.

    __init__(self, name, house): This is the constructor method. It takes three parameters:

    self: This parameter is a reference to the instance of the class itself. 
            It is used to access and modify attributes and methods of the object.
    name: This parameter is used to pass the name of the student when creating a new instance.
    house: This parameter is used to pass the house of the student when creating a new instance.
    Inside the __init__ method, self.name and self.house are attributes of the class Student. They store the name and house of each instance of the class.

    In summary, the __init__ method is responsible for setting initial values for the attributes of a newly created instance of the Student class. This allows you to customize each instance with specific data when it is created.
"""

# If the user enters nothing but space as the input.

class Student:
    def __init__(self, name, house):
        if not name:                        # This is more pythonic and it's the same as "if name = '' "
            print("Missing name.")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()

# But this is not good enough. It does not suffice to just print out missing name and then the rest of the code go through.
# What can we do instead then.

# We could use 'sys.exit' and say something like 'missing name'

import sys

class Student:
    def __init__(self, name, house):
        if not name:                        
            sys.exit("Missing name.")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()

# But this is a really obnoxious solution to this problem.
"""
    Just because the user messed up and called a function with an invalid name, we are gonna quit the  whole program? \
    That's really extreme of a response.
    We don't want to exit the program in some arbitrary line just because the input was invalid.

"""

# We do now have a mechanism for signaling errors.

# Unfortunately we can't do something like this_


class Student:
    def __init__(self, name, house):
        if not name:                        
            return None                         # We can't do something like this.
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()

# Because it's actually too late to return none.
# If we see after some lines, we can see that the 'student = Student(name, house)'.
# The student is already created. There is an object somewhere in the computers memory that is stuctured as a student and it just hasn't any values inside of it.

# So the object exists. So we can't say that it doesn't.

# So it's up to us to signal an error.

# It's time we create our own errors.


# It turns out in python there is another keyword related to exceptions that python itself uses to all those exceptions.

# Like ValueError or other such exceptions to come with python. We are now going to raise them by ourselves when something goes wrong.
# But not wrong enough that we want to quit and exit the whole program but enough that we need to somehow alert the programmer that there has been an error.


class Student:
    def __init__(self, name, house):
        if not name:                        
            raise ValueError                        # We are now calling the ValueError.
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()

# We can even be more precise. We don't have to raise a generic ValueError and let the programmer figure out what went wrong.

# We can treat ValueError and all exceptions in python like functions and actually pass to them an explanatory messege like quoted messeges like this.

class Student:
    def __init__(self, name, house):
        if not name:                        
             raise ValueError("MIssing Name")       # We have now left the messege with the error.                  
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()



# We are now making the demands in respect of houses.

class Student:
    def __init__(self, name, house):
        if not name:                        
             raise ValueError("MIssing Name") 
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house.")                       
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()

# And that's how we are now creating our own errors and telling the user what is wrong with the input.

"""
    So here we now see a capability that we can do with classes that we can't with dictionaries.
    If we add a key/attribute to a dictionary then it's going nowhere. Evem if the name is empty or the house is a completely random string of text it's still going into that dictionary.

        But with a class and by the way of this init method we can now control excatly what is going to be installed if we will inside of this object.
            We have more control now over the correctness.
            
"""

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()

"""
    This defines a class named Student.
    It has two methods: __init__ and __str__.
    __init__ is a special method (constructor) that initializes the attributes of a Student object when it is created.
    __str__ is another special method that specifies how an instance of Student should be represented as a string when printed.


    The __init__ method takes four parameters: self, name, house, and patronus.
    self is a reference to the instance of the class itself.
    It checks if name is provided and if house is one of the valid options: "Gryffindor", "Hufflepuff", "Ravenclaw", or "Slytherin".
    If the checks pass, it initializes the attributes name, house, and patronus for the object.

    ___str__-
        This method overrides the default behavior of how a Student object is converted to a string.
    When you print a Student object, it will return a string formatted as "{name} from {house}".
    
    main()-
    The main function is the entry point of the program.
    It calls the get_student function to create a Student object and then prints it.
"""

# Now we are going even one more step further.
"""
    What if we want to create more functionality for a student so that your class really represents this real world/fantasy world,
        Where students not only have names and houses or patronuses, they also have functionality.
            They have actions they can perform like casting a charm/ a spell.
"""
# Now we are implementing a function called charm.
# Let's define our very own function as follows.


class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()


class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell Terrier":
                return "😹"   
            case _:                                 # If self.patronus does not match any of the previous cases ("Stag", "Otter", or "Jack Russell Terrier"), this catch-all case will be triggered, and the function will return "/".
                return "/"             

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()

"""
    print(student.charm()): This line calls the charm() method of the Student object student.
      This method is responsible for determining and returning the emoji associated with the patronus.
      The result is then printed to the console.

    Overall, these lines orchestrate the flow of the program.
      They prompt the user for input to create a Student object, 
      display a message, and then print the emoji associated with the patronus.
"""


# We can even override the input like this.

# As it turns out with classes and objects thereof you are I can still access those instance variables using this familiar dot notation.
# So we can actually change them later if we want.
# And this will effectively circumvent the if condition and the other if condition in our init method.
    # Because that is only called when we first create the student object,

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

               

def main():
    student = get_student()
    student.house = "120, Baker street, New york."      # There is nothing stopping me at the moment to change the house or the name after.
    print(student)
    

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()

# FYI_ In the 5th line of code we made a ValueError code.
# So, how this code actually runs is, we have to make sure that the input actually matches the demand. Otherwise it's going to show the ValueError.
# Then still the input is going to be overridden.

# In the spirit of programming a little more defensively allow me to introduce another feature of python as well namely "properties"
"""
    So property is really an attribute that has even more defence mechanisms put into place.
    A little more functionality implemented by you to prevent programmers like me and you for messing things up like this attribute.

        Properties is going to be an attribute where we are going to have more control over.

"""
# We are going to implement them like this "@property" which is technically a function property in python 
# We are going to see some new 'at syntax' that allows us to decorate functions and this too is a term of art in the world of python.

# What we are saying is, in python we can have decorators which are functions that modify the behavior of other functions if you will.

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
# Getter
    def house(self):
        return self.house
# Setter
    def house(self, house):
        self.house = house 

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()


# let's try it another way.

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
# Getter
    @property
    def house(self):
        return self._house
# Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house 

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

# Here's a step-by-step explanation of the code:
"""
    1. Class Definition:
        class Student:
        Defines a class named Student.

    2. Constructor Method:

            def __init__(self, name, house):
                if not name:
                    raise ValueError("Invalid name")
                self.name = name
                self.house = house
    The __init__ method is the constructor method, which initializes a new instance of the class.
    It takes two parameters: name and house.
    It first checks if the provided name is not empty. If it is empty, it raises a ValueError.
    It then assigns name and house to the respective attributes of the instance (self).
    Note: In the original code, self.house is used to call the setter method. This could lead to a recursive call and an error. I've corrected it in the explanation

    3. String Representation Method:
            def __str__(self):
                return f"{self.name} from {self.house}"
    The __str__ method defines how the class should be represented as a string when using print or similar functions.
    In this case, it returns a formatted string containing the name and house of the student.

    4. Getter Method using Property:
            @property
            def house(self):
                return self._house
    This is a getter method for the house attribute.
    The @property decorator is used to define a method as a "getter". It allows you to access the method like an attribute.
    The getter returns the value of the private attribute _house.

    5. Setter Method using Property:
        @house.setter
        def house(self, house):
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self._house = house 
        This is a setter method for the house attribute.
        The @house.setter decorator is used to define a method as a "setter".
        The setter method takes a parameter house, representing the new value.
        It first checks if the provided house is one of the valid options. If not, it raises a ValueError.
        If the value is valid, it assigns it to the private attribute _house.

    
    6. Main Function and User Input:
         def main():
            student = get_student()
            print(student)
        The main function is defined to demonstrate the usage of the Student class.
        It calls the get_student function to get user input for creating a student instance and then prints it.
    

    7. Function to Create Student:
         def get_student():
            name = input("Name: ")
            house = input("House: ")
            return Student(name, house)
        The get_student function prompts the user for a name and house, and then creates and returns a Student object.
     

    8. Running the Program:
            if __name__ == "__main__":
            main()


This block ensures that the main function is executed when the script is run directly (not imported as a module).
Overall, this code defines a Student class with a getter and setter method for the house attribute, ensuring that the house is one of the valid options. It also provides a way to create a Student object and print its information.
           

        
"""



# If we run the program now then, we are still going to see the errors.
"""
    Let's type in gryffindor which will at least pass our checks that's induced by init.
    But the line 24 is going to trigger the same setter to be called and the ValueError is going to be raised.

"""
# What is the solution to that then?
# We can change the 'student.house' to the 'student._house'
# Because the instance variable is now called the '_house'. The property is called 'house' no '_'. 

# But the "_" attribute implemented as an instance variable is still called 'underscore house'


# Now if we run the code then_

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
# Getter
    @property
    def house(self):
        return self._house
# Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house 

def main():
    student = get_student()
    student._house = "Number Four, Privet Drive"     # We added the underscore to make sure that it is an instance variable. 
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
# Now we slipped through the ValueError.

"""
    Python itself allows you to specify that certain instance variables can be public and accessible to anyone's code.
    Or protected or private which means that no one else should be able to change this values

    That's the underscore.
        In python if a instance variable starts with an underscore starts with an underscore_
            DON'T TOUCH IT.
        The underscore is meant to signify a convention that this is meant to be private but it really means 'please don't touch this.' 

    
    Sometimes there is 2 underscores which we can use too.
        That's even greated effort by the coder to say "REALLY DON'T TOUCH THIS".
    But there is nothing in python which is stopping you or me from circumventing all of these mechanisms.

        
"""

"""
    Single Underscore Prefix _var:

    A single underscore at the beginning of a variable or method name (_var) is a convention indicating that the variable or method is intended for internal use or it's a non-public part of the API.
    It's a signal to the programmer that this variable or method is considered "protected" and should not be accessed directly from outside the class/module. However, it's not enforced by the Python interpreter.
    
    
    Double Underscore Prefix __var:

    A double underscore at the beginning of a variable name (__var) triggers name mangling. Python will rename the variable in a way that makes it harder to create subclasses that accidentally override private attributes and methods.
    This is not to make it "private" in the strictest sense, but rather to avoid name conflicts in subclasses. The actual name is transformed to _classname__var, where "classname" is the name of the current class. This makes it less likely that a subclass will accidentally override a private attribute.
"""

# It might come as quite a surprise that even though might have identified OOP by name now.
# But we've all been using classes and objects forever now in this class.

"""
    In fact if we think back on one of the very first things we did in the class, we used integers.
    And just got integers from the user.
        But if we see the docutmentation for integers_ "docs.python.org/3/library/functions.html#int"
            We can actually find int itself is and has been for weeks a class and in fact this is the signature of the constructor call for an INT
"""
"""
    In fact_ "class int(x, base=10)"
    This is the signature of the constructor  call for an int where by we pass in x 
"""

# Strings too are also a class. If you have used str.lower(), 
# you were using a method that came within the str class. 
# You can learn more in Python’s documentation of str.


# list is also a class. Looking at that documentation for list, you can see the methods that are contained therein, like list.append().
# You can learn more in Python’s documentation of list.

# dict is also a class within Python. You can learn more in Python’s documentation of dict.

# To see how you have been using classes all along, go to your console and type code type.py and then code as follows:
print(type(50))

# We are going to see something like this "<class 'int'>"
# Notice how by executing this code, it will display that the class of 50 is int.


    # The program actually prints out the type of the number 50.
        # It is not something we want to show to the user. 

# Write if we write code something like this_
print(type("Hello, world"))
# Now we are going to see something like this_"<class 'str'>"
    # There it is. We can now see that the str is also a class

# We can do this a lot of staffs_
print(type([]))
# Now we are going to see something like this_"<class 'list'>"
    # There it is. We can now see that the list is also a class

# We might recall we can create an empty list by literally doing this_
print(type(list()))
# Here we go again_"<class 'list'>"
    
# Let's do dictionary then_
print(type({}))
# This code will indicate this is of the class dict

# As the list we can just do the same here too.
print(type(dict()))
# This code will also indicate this is of the class dict.

# Sometimes, wa want to add functionality to ac class itself,l not to instances of that class.

# "@classmethod" is a function that we can use to add functionality to class as whole.

import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

hat = Hat()         # Here we instantiated a hat object.
hat.sort("Harry")    # If we do this let's propose that it prints out what house that student should be in.

# We created a variable called hat in lower case and instantiate a hat object.

# So no matter what the hat class ends up with, this is the common syntax for instantiating an object of a certain class.
 

"""
    def sort(self, name):: This defines a method named sort which takes two arguments: self (implicitly passed and refers to the object itself) and name. 
    This method will be used to sort a person into a Hogwarts house.

    print(name, "is in", random.choice(self.houses)): This line prints a message indicating the name and the randomly selected Hogwarts house. 
    random.choice(self.houses) is used to randomly select one of the four houses.
"""

# hat = Hat(): This line creates an instance of the Hat class and assigns it to the variable hat.

"""
    hat.sort("Harry"): This line calls the sort method on the hat object, passing the string "Harry" as the name argument. 
    This will randomly select a Hogwarts house and print a message indicating which house Harry is sorted into.
"""

import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")


# We could do the same thing this way too.

import random

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


def sort(name):
    print(name, "is in", random.choice(houses))


sort("Harry")

# And it still works

# What we are trying to do is, we are actually trying to different way of meodeling the world.

# And no it seems too simple and it's not truely compeling.
# But when we getting more advance and start to colaborate wit other people's code then the code actually becomes messy.
# That's where the 'class' actually comes. It organizes the code.

# Let's go into the Harry Potter world try to make classes for student names, teacher's name, houses, where they are from and all that.


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    
    @classmethod
    def get(cls):                      # We have to give it at least one argument, in this case 'cls'
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)        # It's an automatically reference to the class itself.

def main():
    student = Student.get()     
    print(student)



if __name__ == "__main__":
    main()

# Here the class is actually all of my student specific functionality.
# That is to say if I have functionality and data related to student you the programmer my would assume that it's all bundled up.

"""
    And yet if we scroll down further we can see there is function called get student that exists else where in the file.
    And it prompts the user for a name, prompts the user for a house
        And then it creates the student objects and retuerns the values into it.
        
"""
# We removed the 'get_student' function.
"""
    This might seem weird cause now I am actually calling 'cls' and now I am passing an argument.
    So we did a final fix here by saying that it's a 'classmethod'.
"""
# What are we actually doing here_
"""
    Inside of my student class I now have a function called get. It is I shall claim a class method.
    It means I can call this method with instantiating a student object first.
        There in lies the potential of the chicken in the egg problem.
            We actually did the 'chicken in the egg problem'. Cause_

            It would be weird if I had to create a student object in order to call get/ in order to get another student object ...and that just sounds messy.
                So why don't we just get a student via 'classmethod' which by definition does not require us to create a student object first.

"""

# Here the get functionality is built into the class.
# So we edited the the main function and called out the get method like this "Student.get()"
# The get function is actually built inside the class, so if we call it like this, it should work.

# What if we want to call the main function at the very beginning. Like this_

def main():
    student = Student.get()     
    print(student)

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    
    @classmethod
    def get(cls):                      
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)        

if __name__ == "__main__":
    main()

# But if we run this code this will work but it shouldn't.
# Because the code is actually mentioning student which does not exists. until we go below the code.

"""
    The reason why the code works is because of the second last line of the code.
        Here we are not actually calling the main until the very end.
        It just means python have to read everything from top to bottom. So technically everything exist.

"""

# But still it is cleaner to use it the previous way.
"""
    It turns out that besides @classmethods, which are distinct from instance methods, there are other types of methods as well.
    Using @staticmethod may be something you might wish to explore. While not covered explicitly in this course, you are welcome to go and learn more about static methods and their distinction from class methods.
"""

# Introduction to Inheritence.

# Inheritence is perhaps the most powerful feature of object oriented programming.

"""
    Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class (the child or subclass) to inherit attributes and methods from another class (the parent or superclass). 
    This enables the child class to reuse and extend the functionality of the parent class.
"""

# It just so happens that you can create a class that “inherits” methods, variables, and attributes from another class

# Both students and professors are at the end of the day wizards. So now we combined both of the classes.
# We defined a third class for instance called wizaed that has any of the common attributes for students and professors

# But the only thing they have in common is a name and a name in student and professor respectively.
# Let's factor that out first.

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name.")
        self.name = name                        # We can only adding name because the common thing between professors and students is name. Not house or subject.
    ...

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name.")
        self.name = name
        self.house = house

    ...

class Professor:
    def __init__(self, name, subject):
        if not name:
            raise ValueError("Missing name.")
        self.name = name
        self.subject = subject

    ...


# Now that we aded 3 classes, we don't have to raise the ValueError in every class. 
# Also we can now remove the assignment 'self.name = name' because we are doing that in wizard. 

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name.")           # We don't have to raise ValueError because we brought the names from other classes in here. So, if we check this, we are actually checking every classes. And same goes for 'self.name'
        self.name = name               
    ...

class Student:
    def __init__(self, name, house):
        self.house = house

    ...

class Professor:
    def __init__(self, name, subject):
        self.subject = subject

    ...
# How do we now link these 2 classes together.

# The way we can prescribe inheritance where by one class should inherit from another, we can do something like this.

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name.")           
        self.name = name               
    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)                                     # It is a reference to the super class of this class.
        self.house = house

    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...
wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")                                # We fixed the values
professor = Professor("Severus", "Defence Against the Dark Arts")

# Here a student inherits from or is a subclass of wizard which conversely is the superclass of the student class.

# The 'Student(Wizard)' means when I define a student class go ahead and and inherit all of the characteristics of the Wizard as well.
# We are going to do the same thing for professor too.

# Also we want to fix that we also want to use the functionality in the wizard classes init method.

"""
    The way to do that is as follows.
    Let's go to the init method of the student. And we are going to call a funtion called "super()"

    So if this class if Student the super class aka the parent class is wizard. We are now actually connected with the super class but now we have to access into the objects.

    To do so_
    we did this 'super().__init__(name)'
        By this we accessed the init method of the super class and called the name of the class.
    And we are gonna do the same in the Professor class.

"""
# While we have just introduced inheritance, we have been using this all along during our use of exceptions.

# It just so happens that exceptions come in a heirarchy, where there are children, parent, and grandparent classes. These are illustrated below:
"""
BaseException
 +-- KeyboardInterrupt
 +-- Exception
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- KeyError
      +-- NameError
      +-- SyntaxError
      |    +-- IndentationError
      +-- ValueError
 ...
    
"""
# Some operators such as + and - can be “overloaded” such that they can have more abilities beyond simple arithmetic

# For example "+" is never used for just addition per say, we use it for joining two strings.

# To understand more about this let's suppose a bank in the harry potter world.
# And the type of money that exists in the world of harry potter are called galleons and sickles and canucks.(They are in descending order of value)


# Let's create a class called "Vault"
# When we create a vault and create create the arguments (types of money) I want to initialize it with some number of galleons, sickles and some number of Canucks.

# The programmer is able to pass in one or more of those values ideally but they can be optional. So we'll give them default.
 

class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):       # It is saying the default values are zero. The programmer can set it to whatever number they want.
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
            # Now the values are passed in.

# Let's create a Vault for potter.

potter = Vault(100, 50, 25)     # It means potter has 100 galleons, 50 sickles, 25 knuts.
print(potter)

"""
    If we print it this way the program seems to work and no syntax errors or something. But we are not getting the perfect output.

        That is because the objects of the vault is not in sting.
        We have to print it in the string format.

        So we need to put "__str__" method into the program.

"""
class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
            # Now the values are passed in.

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts. "


potter = Vault(100, 50, 25)     # It means potter has 100 galleons, 50 sickles, 25 knuts.
print(potter)

# Now if we run the code, Now we see everything is perfectly shown as the output.

# Let's create a weasley variable into the program along side the potter variable. 
class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
            

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts. "


potter = Vault(100, 50, 25)     
print(potter)

Weasley = Vault(20, 70, 35)     
print(Weasley)

# Let's do a total of them both. 
class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
            

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts. "


potter = Vault(100, 50, 25)     
print(potter)

Weasley = Vault(20, 70, 35)     
print(Weasley)

# It works perfectly.


galleons = potter.galleons + Weasley.galleons
sickles = potter.sickles + potter.sickles
knuts = potter.knuts + Weasley.knuts                    # Here we actually override the variables.

total = Vault(galleons, sickles, knuts)     # Here we passed in new variables.
print(total)

# And still the code works. 

class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
            

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts. "

    def __add__(self, other):
        galleons = self.galleons + other.galleons           # The 'self.galleons' is for potter and the 'other.galleons' is for weasley's.
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)     
print(potter)

Weasley = Vault(20, 70, 35)     
print(Weasley)

total = potter + Weasley 
print(total)

"""
    The code encapsulates the addition logic within the __add__ method. If there are changes to the addition logic in the future, 
    you only need to update one place (the __add__ method).
"""
"""
    How the code works_
        The "__add__" method actually works as the addition operator.
        When we do "total = potter + Weasley" then python actually wants to add the Vaults.
            And that is where the "__add__" method comes. When the "+" sign comes then python calls out the __add__ method.
            Where the objects of the class becomes additioned.

 """

students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Ron", "house": "Ravenclaw"}
]

houses = []                                     # We could also use 'list()'
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])
for house in sorted(houses):
    print(house)


# Here we had to do the 'if else' into the code.
# What if we don't want do that.

# We can to the code this way.
# It turns out we can use the built-in set features to eliminate duplicates.

students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Ron", "house": "Ravenclaw"}
]

houses = set()                                     
for student in students:
    houses.add(student["house"])
for house in sorted(houses):
    print(house)

# Notice how no checking needs to be included to ensure there are no duplicates.
# The set object takes care of this for us automatically.


"""
    In some languages there is a notion of global variables. Where by we can define a variable that's either local to a function
    Or if we put a variable outside of all of your functions perhaps perhaps near the top of you file,
        That would generally be considered a global variable.
"""
balance = 0

def main():
    print(f"Balance: {balance}")
    deposite(100)
    withdraw(50)
    print(f"Balance: {balance}")

def deposite(n):
    balance += n

def withdraw(n):
    balance -= n 

if __name__ == "__main__":
    main()

    # If we do this we will see a new error called "UnboundLocalError".
    # The error says "cannot access local variable 'balance' where it is not associated with a value"

    # Which is kinda misleading cause We absolutely assigned balance of value.
"""
    What python is actually saying it to us is if we actually want to change the change the value_
        It might need to be local to the function.
    
    If we are trying to change a global variable in a function it clearly does not works.
        It is okay to read the variable but we can't write to it in the same way.

"""

# The is a keyword in python called global that allows you to tell a function that this is not a variable that is local to you.
# And we want it to be a global variable that we want the function to edit.

# The try the code again 



balance = 0

def main():
    print(f"Balance: {balance}")
    deposite(100)
    withdraw(50)
    print(f"Balance: {balance}")

def deposite(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n 

if __name__ == "__main__":
    main()

class Account:
    def __init__(self):
        self._balance = 0           

    @property                               # We used "@property" because we want to remind ourselves that it is the property of the class.
    def balance(self):
        return self._balance


# We used the underscore "_" in "_balance" to effectively indicate that it's private.
        # It's just an indication to ourselves that this is something that we shouldn't touch or other code shouldn't touch, just functions in this class now 

    def deposite(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n 

# We are now going to create an account object by calling the account Constructor which is the name of the class.

def main():
    account = Account()
    print(f"Balance: {account.balance}")
    account.deposite(100)
    account.withdraw(50)
    print(f"Balance: {account.balance}")

if __name__ == "__main__":
    main()

# Let's try something new.

def meow(n):
    for _ in range(n):
        print("meow")

number = input("Number: ")
meow(number)

# What is wrong in this code?

# We can see a new error and it is saying_
"""
    Exception has occurred: TypeError
        'str' object cannot be interpreted as an integer
"""

# It's saying that the given input is in an string format.
# How do we usually solve this problem?

# We just turn it into the 'int' while taking the input as usual. But there is a new way to do this.

def meow(n: int):
    for _ in range(n):
        print("meow")

number = input("Number: ")
meow(number)

# Still we can see an error while says the following_
"""
    Exception has occurred: TypeError
        'str' object cannot be interpreted as an integer
"""
# But let's try this in "mypy" program.
"""
    It is an example of a program that understands type hints and if we run i proactively ourselves_
        we can fund bugs like this in my code before I or worse a user actually runs and encouters something cryptic
    Like this TypeError here.

"""
# To use mypy we are going to go to the terminal window and we are going to type in "mypy meows.py"( The name of the file)

# By this the user can get the exact information about what is wrong with the writter code.

def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = input("Number: ")
meow(number)
# If we use this then still we'll see the same error.

def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)

# So we can fix the code this way.
# If we try something like this_

def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

"""
    We will see something like this_
        meow
        meow
        meow 
        None
"""
# As it turns out our meow function only has a side effect. It just prints out meow a number of times.
# It doesn't have any returned value.

# As it turns out our meow function only has a side effect. It just prints out meow a number of times.
# It doesn't have any returned value.

# As if it would if there were literally the return keyword.
# By default then when a function in python does not explicitly return a value it's ip.icit return value is effect "None".
# So what we are seeing here is in line 8, because we are assigning the return value of meow 
# Which is none to our meow variable, so the line 8 is now incorrectly printing None.

# Because we accidently thought that 'meow' returns a value but it doesn't so the returned value of it is none.


# So how can we go about catching this kind of mistake too?
# We might make this mistake but may be with less frequency if I'm in the habit of annotating my code with this new feature called 'type hints'

# Here is how we implement the feature.

def meow(n: int) -> None:           # It means that our meow function by design returns None.
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
