'''
Created on 06-Apr-2025

@author: Vivek

List: Is a data structure represented by []

1. Creation of list
    - Empty list can be created
    - List with elements:
        > Manually adding elements
        > Using in-built function called list()
2. List is heterogeneous
3. Accessing elements
    - Indexing/ Using Index
    - Using slicing operator
4. List can be modified


slicing operator- list_name[start : stop : step] -> takes index as input
Default values:
start: Index 0
stop: last index
step: 1

start should be greater than stop
'''

#1. Creation of list
# a. Creation of empty list
a = []
print(type(a))

# b. Creation of list with elements
b=[1, 2, 3, 4, 5] # homogenous data structure
print(type(b))
print(b)


c=[1, "abc", 4.76, True, 3+8j] # heterogeneous data structure
print(c)

d=list(range(1, 20))
print(d)

# Accessing the elements using Index
print(c[4])
print(c[-1])

# Modification/ replacement using index
c[1]="Vivek" # re-initialization
print(c)


# slicing operator- list_name[start : stop : step] -> index
print('d[::]-->', d[::])
print('d[3:9]-->', d[3:9])
print('d[:12]-->', d[:12])
print('d[6:]-->', d[6:])
print('d[-12:-6]-->', d[-12:-6])
print('d[::2]-->',d[::2])
print('d[::-1]-->',d[::-1])
print('d[-6:-12:-1]-->',d[-6:-12:-1])
