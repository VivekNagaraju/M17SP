'''
Created on 26-Apr-2025

@author: admin
'''
'''
for j in range(6): # j represents rows
    for i in range(6): # i represents stars
        print("*", end=" ")
    print()
'''
'''
name=input("Enter your name:")


print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print("Negative indexing")
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])

# print(len(name))
index=-1
reverse_string=""
while index>-(len(name)+1):
    reverse_string=reverse_string+name[index]
    index=index-1
    
print(reverse_string)
'''

#Left-half pyramid
'''
    *
   **
  ***
 ****
*****
'''

for j in range(5): # j represents rows; switching lines
    for k in range(5-j): # printing spaces
        print(" ", end=" ")
        
    for i in range(j): # printing stars
        print("*", end=" ")
    print()
