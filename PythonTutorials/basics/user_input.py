'''
Created on 29-Mar-2025

@author: Vivek
'''
while True:
    a=float(input("Enter a number:"))
    b=float(input("Enter another number:"))
    c=a+b
    print(f"Addition of {a} and {b} is " , a+b )
    d=input("Do you want to continue?(Y/N):")
    if d == 'N':
        break