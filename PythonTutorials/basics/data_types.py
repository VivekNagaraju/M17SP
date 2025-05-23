'''
Created on 25-Mar-2025

@author: Vivek

Data type: category to which an i/o data belongs to.

Categorization of data helps us in memory allocation for efficient memory handling.
To check the compatibilty b/w 2 data types

Q. Dynamic typing vs Static typing

Categories of data-types:
1. Built-in data-types: Data types already available in python
    a. Fundamental/ primary data types:
        i. int
        ii. float - decimal numbers
        iii. complex - a+bj
        iv. bool (boolean) - True or False
        v. str (string) - "",'', ''' '''
        
    b. non-fundamental data types:
        i. list
        ii. tuple
        iii. set
        iv. dict
        v. bytes
        vi. bytearray
        
2. User defined data types: Data types which are created by programmer

Commenting in Python:
1. Single line comments - #
2. Multi line comments - triple double/ single quotes.
'''
# int a = 3; --> java example
a = 3.65 # float
b = "vivek" # str
c = 5 # int
d = 4+7j # Complex
e = True # bool
# c = a+b
# print(c)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# print(type(c))

#Type Conversion/ Type casting
print("=======Type casting=======")
f = int(3.65) # o/p: 3 -> int
print(f)
print(type(f))

# float()
# str()
# complex()
# bool()

g=str(100)
print(g)
print(type(g))

h='60'
print(h)
print(type(h))

print(g+h) # Concatenation: combining 2 strings





