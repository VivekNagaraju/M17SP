'''
Created on 12-Apr-2025

@author: Vivek

Dictionary: Collection of Key-value pairs

dict_name={key1:value1, key2:value2, key3:value3...}

1. Empty dictionary can be created
2. Dictionary doesn't allow duplicates elements
3. Dictionary allows duplicate values but not keys
'''
d1={}
print(d1)
print(type(d1))

stds={1:'Bhavani', 2:'Chitra', 3:'Sandeep', 4:'Sanjana', 5:'Yogitha'}
print(stds)
print(type(stds))


d2=dict() # Creates Empty dictionary
print(d2)

d3=dict.fromkeys([1, 2, 3, 4], "xyz")
print(d3)

iquest_students2={'Bhavani':1, 'Chitra':2}
print(iquest_students2)



print(stds[3])
print(iquest_students2['Bhavani'])

print(stds.keys())
print(stds.values())

for ele in stds.values():
    print(ele)

d4={1:'Bhavani', 2:'Chitra',  3:'Chitra'}
print(d4)

d4[3]='Sanjana'
print(d4)

d4[4]='Yogitha'
print(d4)

d5=d4.copy()
print(d5)

print(d4.items())

print(d4.pop(2))
print(d4)

print(d4.popitem())
print(d4)

print('d3-->',  d3)
print('d4-->', d4)
d4.update(d3)
print('Updated d4',d4)