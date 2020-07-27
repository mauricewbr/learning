#This is going to document my Python learning journey

# 1 Python basics

#INTEGERS

myint = 7

#FLOATS

myfloat = 7.0
myfloat = float(7)

#STRINGS

mystring = "hello"
mystring = 'hello'
lotsofhellos = "hello" * 10

#String formatting
name = "John"
age = 23
#print("%s is %d years old!")
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right dot.
# %x/%X - Integers in hex representation (lowercase/ uppercase)

#Length of string
astring = "Hello world!"
length = len(astring)

#Index of input
astring = "Hello world!"
index = astring.index("o")

#Character count
astring = "Hello world!"
count = astring.count("l")

#Slice of string
astring = "Hello world!"
slice = astring[3:7]

differentslice = astring[3:7:2]
#Skipping every 2nd character

#Reversing a string
astring = "Hello world!"
reversedstring = astring[::-1]

#Uppercase/ lowercase conversion
astring = "Hello world!"

#Starting point/ Ending point
astring = "Hello world!"
astring.startswith("Hello")
astring.endswith("asdadsasds")
#Will return True/ False

#Splitting a string
astring = "Hello world!"
split = astring.split(" ")

#OPERATORS

#Addition
one = 1
two = 2
three = one + two

#Multiplication
number = 1 + 2 * 3
squared = 7 ** 2

#Modulo
remainer = 11 % 3
#returns 2

#String operators
hello = "hello"
world = "world"
helloworld = hello + " " + world

#List operators
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
biglist = [1,2,3] * 3

a, b = 3, 4

#LISTS

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
#mylist now contains 1,2,3

#CONDITIONS

x = 2
# print(x == 2) prints True
# print(x == 3) prints False
# print(x < 3) prints True

#Boolean operators
name = "John" 
age = 23 
if name == "John" and age == 23:
	pass
if name == "John" or name == "Rick":
	pass

#The 'in' operator
name = "John"
another_statement = False
if name in ["John", "Rick"]:
    pass
elif another_statement is True:
    pass
else:
    pass

#The 'is' operator 
x = [1,2,3]
y = [1,2,3]
# print(x == y) prints True
# print(x is y) prints False

#The 'not' operator
# print(not False) prints True
# print((not False) == (False)) prints False

#LOOPS

#The 'for' loop
primes = [2,3,5,7]
for prime in primes:
    continue
for x in range(3,7):
    #prints 3,4,5,6
    continue
for x in range(3,7,2):
    #prints 3,5
    continue

#'while' loops
count = 0
while count < 5:
    count += 1

#'break' and 'continue' statements
#'break' ist used to exit a for loop or a while loop, whereas continue is used to skip the current block and return to the 'for' or 'while' statement

count = 0
while True:
    count += 1
    if count >= 5:
        break

for x in range(10):
    if x % 2 == 0:
        continue

#'else' clause for loops

count = 5
while (count < 5):
    count += 1
else:
    #print("count value reached %d" %(count))
    pass

for i in range(1, 10):
    if (i % 5 == 0):
        break
else:
    #print("this is not printed because for loop is terminated because of the break statement but not due to fail in condiction")
    pass

#FUNCTIONS

def my_function():
    pass
def my_function_with_args(argument1, argument2):
    pass
def sum_two_numbers(a, b):
    return a + b

my_function()
my_function_with_args("name", "second name")
sum_two_numbers(1, 2)

#CLASSES AND OBJECTS

class MyClass:
    variable = "blah"

    def function(self):
        pass

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "Hello"

myobjectx.variable
myobjectx.function()

myobjecty.variable

#DICTIONARIES

#Initialization
phonebook = {}
phonebook["John"] = 1234134
phonebook["Jack"] = 2334233
phonebook["Jill"] = 2345234

phonebook = {
    "John" : 12341234,
    "Jack" : 23452354,
    "Jill" : 43535423,
}

#Iterating over dictionaries
phonebook = {"John" : 13123412, "Jack" : 12423423, "Jill" : 345634564}
for name, number in phonebook.items():
    #print("Phone number of %s is %d" % (name, number))
    continue

#Removing a value
del phonebook["John"]
phonebook.pop("Jack")

#MODULES AND PACKAGES

#Importing module objects to the current namespace
#from draw import draw_game

#Importing all objects from a module
#from draw import *

#Custom import name
if True:
    #import draw_visual as draw
    pass
else:
    #import draw_textual as draw
    pass

#Extending module load path
#PYTHONPATH =/ foo python game.py
#Sys.path.append should be executed BEFORE running an import command
#sys.path.append("/foo")

#Exploring built-in modules
#https://docs.python.org/3/library/
#When importing libraries, the implemented functions can be viewed with 'dir(implemented_library)'
#When in need of more information on certain functions, 'help' can be used as 'help(implemented_library.function)

#Writing packages
#each Python package MUST contain a __init__.py file
#That file can be empty but can instead also define which module the package exports as the API:
#__init__.py:
#__all__ = ["bar"]


#NUMPY ARRAYS

#Setup
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

#Element-wise calculations
bmi = np_weight / np_height ** 2

#Subsetting
bmi > 23 #For a boolean response
bmi[bmi > 23] #for only those observations above 23

