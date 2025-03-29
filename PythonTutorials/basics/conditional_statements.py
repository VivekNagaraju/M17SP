'''
Created on 29-Mar-2025

@author: Vivek

Conditional statements: Statements which check the conditions and determine the flow

If a condition is satisfied one set of code will executed otherwise another set of code can be 
executed

Syntax:

if (condition):
 <code to be executed if condition is satisfied>

Indentation
'''

age=int(input("Enter your age:"))

"""
if age>=18 and age<=59:
    print("You're an adult")
    
elif age<18 and age>12:
    print("You're an adolescent")

elif age<13:
    print("You're a child")
    
else:
    print("You're a senior citizen")
"""
'''
if age>18:
    if age<=59:
        print("You're an adult")
        
    else:
        print("You're a senior citizen")
else:
    if age>=13:
        print("You're an adolescent")
        
    else:
        print("You're a child")
'''
if age>=0:
    if age in range(0, 13):
        print("You're a child")
    
    elif age in range(13, 19):
        print("You're an adolescent")

    elif age in range(19, 60):
        print("You're an adult")
    
    else:
        print("You're a senior citizen")
else:
    print("Please enter positive number")

