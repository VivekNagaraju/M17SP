'''
Created on 27-Apr-2025

@author: Vivek

Function: Is a block of code which can be reused
OR
Function is a block of reusable code

Ex: print(), type(), input(), id()...

Types of functions:
1. Predefined functions- came as part of python package
2. User-defined functions- are defined by users

Why we need functions?
1. Reduce repetition of code/ reduce complexity, minimize the no. of lines of code. This helps in increased code readability
2. Easy maintanence

Syntax:

def function_name(parameters):
    <code>

def -> keyword to define function (mandatory)
function_name -> lower case words separated by _ (mandatory)
(): -> mandatory
parametrs -> variables to accept/ consume the values passed by the user (not mandatory)

Types:
1. Function without parameters
2. Function with parameters
'''

a=2
b=5
c=a+b 
print(f"Sum of {a} and {b}:", c)

a=6
b=7
c=a+b 
print(f"Sum of {a} and {b}:", c)

# Function without parameters
def welcome():
    print("Hello User! Welcome to iQuest!")
    print("I hope you're doing great!")

welcome()
# welcome()
# welcome()
# welcome()


#Function with parameters
def addition(a, b):
    c=a+b 
    # print(f"Addition of {a} and {b}:", c)
    return c
    
d=addition(10, 20)
print(d)

print(addition(8, 10))


def multiplication(num,multiplier):
    result_mul=num*multiplier
    print(result_mul)
    
multiplication(d, 5)



