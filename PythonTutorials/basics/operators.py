'''
Created on 27-Mar-2025

@author: Vivek

Operator: A symbol which performs operation on operands (variables)
Ex:
10+20 --> addition operation
10, 20 --> operands
+ --> operator
Classification based on number of operands:
1. Unary Operator: performs operation on single operand/ variable Ex: a=-10
2. Binary Operator: performs operation on two operands/ variables Ex: a=10+20
3. Ternary Operator: performs operation on three operands/ variables

Classification based on operations: (Types of Operators)
1. Assignment Operator: =
2. Arithmetic Operators: +, -, *(multiply), /(division), %(moduls), **(exponent), //(Integer division)
3. Relational/ Comparison Operators: >, <, ==, !=, <=, >=
4. Logical Operators: AND, OR, NOT(unary)
5. Membership Operators: in, not in
6. Identity Operators: is , is not
7. Unary minus operator: -
'''
print("=========Arithmetic Operators=========")
a=50
b=50
c=a+b
print(f"addition of {a} and {b}:",c)
print(f"difference b/w {a} and {b}:",a-b)
print(f"multiplication of {a} and {b}:", a*b)
print(f"division of {a} and {b}:",a/b)
print(f"modulus of {a} and {b}:",a%b)
print(f"Integer division of {a} and {b}:",a//b)
print(f"square of {a}:",a**2)
print(f"cube of {a}:",a**3)

print("========Relational/ Comparison Operators=========")
print(f"Is {a} greater than {b}?", a>b)
print(f"Is {a} lesser than {b}?", a<b)
print(f"Is {a} equal to {b}?", a==b)
print(f"Is {a} not equal to {b}?", a!=b)

print("========Logical Operators========")
print("====And Operator====")
print(True and False)
print(False and True)
print(False and False)
print(True and True)

print("====Or Operator====")
print(True or False)
print(False or True)
print(False or False)
print(True or True)

print("====Not operator====")
print(not True)
print(not False)

print("========Membership Operators========")
print("a" in "alpha8678bet")
print("i" not in "alphabet")

print("========Identity Operators========")
print(a is b)
d='vivek'
e='Vivek'
print(d is e)
print(id(a))
print(id(b))
print(id(d))
print(id(e))


