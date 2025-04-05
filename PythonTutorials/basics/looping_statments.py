'''
Created on 01-Apr-2025

@author: Vivek

Looping statements: Statements which executes a code multiple times until a condition is satisfied

Types:
1. While loop:
    a. intialisation of a variable
    b. while condition >> while block
    c. increment/ decrement
2. for loop: iterate over collections/ range

Loop control statements:
1. break- terminate/ stop the execution of loop
2. continue- it skips the execution of loop for once

pass statement: doesn't perform any operations. It is added to make program syntactically correct.

range(start, stop*, step)

1)
*
**
***
****
*****
2)
*****
****
***
**
*

RN | NS
1 | 5
2 | 4
3 | 3
4 | 2
5 |1

Stop Value (6)
row No (1)

No. of stars(5)=Stop Value- row No

3)
1111*
111* *
11* * *
1* * * *
* * * * *

   *
  ***
 *****
*******
'''
'''
count=2.1

while count>0:
    # print("count:",count)
    # print("count<5: ",count<5)
    print("Hello world!")
    # count=count+1
    count-=1 # increment operator: +=; decrement operator:-=

# print("count:",count)
# print("count<5: ",count<5)
'''
'''
while True:
    pass
print("The end")
'''
'''
count=0
while count<=100:
    if count == 50:
        count+=1
        continue
    print(count)
    count+=1
'''

# print(range(10))  
'''
for n in range(1, 100):
    if n == 50:
        continue
    print(n)
'''
'''
for n in range(0, 100):  
    if n%2 == 0:
        if n == 6:
            continue
        print(n)
'''
'''
for n in range(6, 1):
    
    for m in range(n):
        print("*", end=" ")
    
    print()

'''
'''
for n in range(6, 1, -1):
    print(n)
'''
'''
for n in range(5, 0, -1):
    
    for m in range(n):
        print("*", end=" ")
    
    print()
'''
'''
for n in range(1, 6):
    
    for m in range(6-n):
        print("*", end=" ")
    
    print()
'''    
for n in range(1, 6):
    
    for m in range(6-n):
        print(" ", end="")
        
    for i in range(n):
        print("*", end=" ")
    
    print()