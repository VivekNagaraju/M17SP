'''
Created on 04-May-2025

@author: Vivek

Methods are functions which are defined inside a class.
We can call methods using the objects of that class.

A method of one class can be called using an object of that class.

Constructor(__init__): It is a magic method used to construct an Object by initializing it with
specific values being passed while creating the object.
'''

class HumanBeings():
    def __init__(self, name):
        self.name=name
        
    def walk(self):
        print(f"{self.name} is walking")    
        

obj1=HumanBeings("Vivek") 
obj1.walk()

print(type(obj1)) # <class '__main__.HumanBeings'>

obj2=HumanBeings("Yash")
obj2.walk()
obj1.walk()