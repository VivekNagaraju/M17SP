'''
Created on 01-Apr-2025

@author: Vivek

Looping statements: Statements which executes a code multiple times until a condition is satisfied

Types:
1. While loop:
    a. intialisation of a variable
    b. while condition >> while block
    c. increment/ decrement
2. for loop

Loop control statements:
1. break- terminate/ stop the execution of loop
2. continue- it skips the execution of loop for once

pass statement: doesn't perform any operations. It is added to make program syntactically correct.
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

count=0
while count<=100:
    if count == 50:
        count+=1
        continue
    print(count)
    count+=1
    

