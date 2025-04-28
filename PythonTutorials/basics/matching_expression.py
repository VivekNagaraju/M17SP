'''
Created on 26-Apr-2025

@author: admin

match expression:
    case value:
    case value:
'''
day=int(input("Enter day no:"))

match day:
    case 1:
        print("Today is Sunday")
        
    case 2:
        print("Today is Monday")
    
    case 3:
        print("Today is Tuesday")
        
    case 4:
        print("Today is Wednesday")
        
    case 5:
        print("Today is Thursday")
        
    case 6:
        print("Today is Friday")
    
    case 7:
        print("Today is Saturday")
        
    case _:
        print("Enter valid day no.")
