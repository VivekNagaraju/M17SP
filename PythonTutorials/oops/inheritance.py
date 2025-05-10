'''
Created on 07-May-2025

@author: Vivek

Inheritance: Carry forwarding properties from one class to another class.

Parent/ Super class: From which class property is being inherited (Ex: HumanBeings class)  
Child/ sub class: To which class a property is being inherited (Ex: Male class, Female class)

How we can check? 

From object perspective, an object created from a child class should be able to access/ call the 
properties from its parent class

Why we need inheritance?
- It reduces code repetition and increase code reusability which helps us in easy maintanence

Types of inheritance:
1. Single level inheritance
2. Multi-level inheritance
3. Multiple inheritance

Method Resolution Order(mro()): In an inheritance when we call a method using an object MRO 
will helps python interpretor to decide in which order it has to traverse the classes
'''

class GrandFather:
    def __init__(self, name):
        print("Object is created with name:", name)
        
    def gf_method(self):
        print("This is Grand father method")
        
class Mother(GrandFather): 
    
    def __init__(self):
        print("This is mother class constructor")
      
    def m_method(self):
        print("This is Mother method")
        
    def c_method(self):
        print("This is mother class c_method")
        
    def car(self):
        print("This is Mother's car")
        
class Father:
    def f_method(self):
        print("This is Father method")
        
    def car(self):
        print("This is Father's car")
        
class Child(Father, Mother):
    '''
    def __init__(self):
        print("This is child class constructor")
    '''   
    def c_method(self):
        print("This is Child class c_method")

print("======GrandFather Object======")
ajja=GrandFather("ajja")
# ajja.gf_method()

print("======Mother Object======")
amma=Mother("amma")
# amma.m_method()
# amma.gf_method()
# amma.c_method()

print("=======Child Object======")
paapu=Child("paapu")
# paapu.c_method()
# paapu.gf_method()
# paapu.m_method()
# paapu.f_method()
# paapu.car()


print("=======Method Resolution Order(MRO)=======")
print(Child.mro())

print("=======Directory- dir()========")
print(dir(paapu))

