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
    - Using loops
4. List can be modified
5. List stores None as a value
6. List stores duplicate values
7. Insertion order is preserved
8. The size of a list is not fixed or constant

slicing operator- list_name[start : stop : step] -> takes index as input
Default values:
start: Index 0
stop: last index
step: 1

start should be greater than stop

Example exercise: Creating the list of squares of odd numbers
Given list
list2=[]
1. Fetch each element from the given list --> for loop
2. Check whether the element is odd --> if ele%2==1
3. If the element is odd get the square of it --> x=ele**2
4. append the result of step 3 to another list (Create a empty list before step 1) -->list2.append(x)
5. Repeat step 1 to 4 for all elements
6. Print the new list created from the above process. print(list2)
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

# Accessing using loops
print('c-->', c)
# for loop:
print("===For loop===")
for ele in c:
    print(ele)
    
print('===While loop===')

i=0
while i<len(d):
    print(d[i])
    i+=1
'''
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])
'''
# print(len(c)) # Finding the length of a collection

e=["Bhavani", "Chitra", "Sandeep", "Sanjana", "Vivek", "Yogitha", None, "Bhavani"]
print(e)

e.append("Manju")
print(e)

e.insert(5, "iQuest")
print(e)

e.append(c)
print('e.append(c):',e)

f=e.copy()
print(f)



e.extend(c)
print('e.extend(c):', e)

print(len(e))
print(e[10])
print(e[11])

print(e.index(4.76))
print('e.count("Bhavani"):',e.count("Bhavani"))
print('e.index("Bhavani"):',e.index("Bhavani", 1))

'''
Q. Find the indices of a element present in the list
'''

print('c-->', c)
print(c.pop(2))
print(c)
print(c.remove(True))
print(c)
print(c.remove("Vivek"))
print(c)
print('c.pop()', c.pop())
print(c)
c.remove(True)
print(c)