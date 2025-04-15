'''
Created on 14-Apr-2025

@author: Vivek

Strings: word/ phrase/ sentence/ paragraph

letters: Characters in python

Def: String is a character/ collection of characters

Leading spaces: beginning
Trailing spaces: end
'''

name = "VivekNagaraju"

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

print(name.capitalize())
print(name.strip().capitalize())

print(address.casefold())

print(name.count('v'))

print(name.upper())

print(name.find('z'))

# print(name.index('z')) #Raises ValueError when the substring is not found.

print(name.isalnum())
print(name.casefold())
print(name.lower())

print(name.split())

name_list=["My", "Name", "is", "Vivek"]

name_sentence='_'.join(name_list)
print(name_sentence)

print(len(name))

print(name.isalpha())

print(name.isnumeric())

print(name.isalnum())
    
