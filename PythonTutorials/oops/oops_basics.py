'''
Created on 04-May-2025

@author: Vivek

Methods are functions which are defined inside a class.
We can call methods using the objects of that class.

A method of one class can be called using an object of that class.

Method Resolution Order(mro): 

Constructor(__init__): 

- It is a magic method used to construct an Object by initializing it with
specific values/ features being passed while creating the object.

- It is not mandatory to define a constructor. But when constructor is not defined interpretor 
will have its own constructor created

- Calling the constructor: 
    > Constructor is called implicitly during the creation of object
    > Still we can call constructor explicitly
'''

class HumanBeings():
    def __init__(self, name, age):
        self.name=name
        self.age= age
        print("This is constructor", self.name)
        
    def walk(self):
        print(f"{self.name} is walking")    
        

obj1=HumanBeings("Vivek", 32) 
# obj1.walk()
obj1.__init__("Sandeep", 35)

# print(type(obj1)) # <class '__main__.HumanBeings'>

obj2=HumanBeings("Yash", 22)
# obj2.walk()
# obj1.walk()

# print(obj1.name)
# print(obj2.name)
#
# print(HumanBeings.mro())
# print(dir(obj1))

class Car:
    def move_forward(self):
        print("car is moving forward")
        
car1=Car()
# car1.move_forward()
# print(dir(car1))