'''
Created on 14-Apr-2025

@author: Vivek

Strings: word/ phrase/ sentence/ paragraph

letters: Characters in python

Def: String is a character/ collection of characters


'''

name = "vivek"

print("name:", name)
print(type(name))

#Empty string
nick_name=''
print("nick_name:",nick_name)
print(type(nick_name))

age="34" # 34 is considered as a string
print("age:", age)
print(type(age))

#Access using Index
print(name[0])

#Access using for loop
print("===Access using for loop===")
for letter in name:
    print(letter)
 
#Access using slicing operator
print("===Access using slicing operator===")
print(name[1:4])  
print(type(name[1:4])) 

address="""iQuest,

Hebbal Industrial area,

Mysuru.
"""
print(address)

#Modification: String is immutable/ String can't be modified
# name[0]="z" #TypeError: 'str' object does not support item assignment


modified_name=name.replace('v', 'z')
print("name:",name)
print("modified_name:", modified_name)

