# Assingment

# Declaring different types of data types in python
# int
a = 10
print(type(a))

# float
b=99.9
print(type(b))

# complex
c=11+5j
print(type(c))

# string
d="python"
print(type(d))

# list
fruits = ["apple", "banana", "orange"]
print(type(fruits))

# tuple
t=(10,"coders")
print(type(t))

# set
s={"apple","banana","orange"}
print(type(s))

# boolean
bool=True
print(type(bool))

# dictionary
details= {"name": "John", "age": 30}
print(type(details))

# operators
# arithmetic operators

a=10
b=20
# addition
print(a + b)
# subtraction
print(a - b)
# Multiplication
print(a * b)
# division
print(a / b)
# Exponentiation
print(a ** b)
# Modulo
print(a % b)
# Floor Division
print(a // b) 

# Comparison Operators
# Equal
print(a == b)  
# Not Equal
print(a != b)      
 # Greater than
print(a > b)   
 # Less than
print(a < b)      
 # Greater than or equal to
print(a >= b)
# Less than or equal to
print(a <= b)    

# Logical Operators
x = True
y = False
# Logical AND
print(x and y)   
# Logical OR
print(x or y)   
# Logical NOT  
print(not x)     

# Bitwise Operators
c=4
d=8
# Bitwise AND
print(c & d)
 # Bitwise OR
print(c | d)
 # Bitwise XOR
print(c ^ d)
  # Bitwise NOT     
print(~c)      

# Assignment Operators
a = 5
# a = a + 5
a += 5  
print(a)
# a = a - 3
a -= 3  
print(a)
# a = a * 4
a *= 4  
print(a)
# a = a / 2
a /= 2  
print(a)
 # a = a % 3
a %= 3  
print(a)
# a = a ** 2
a **= 2  
print(a)
# a = a // 4
a //= 4  
print(a)

#Conditional Statements in Python
# example of if statement
age = 20
if age >= 18:
    print("you are an adult")
# example of if and else statements
age = 17
if age >= 18:
    print("you are a major")
else:
    print("you are a minor")
# Example of if,elif and else statements
marks = 75
if marks >= 85:
    print("A-grade")
elif marks >= 70:
    print("B-grade")
elif marks >= 55:
    print("C-grade")
else:
    print("Fail")

# Loop Statements in Python:
# for loop
for i in range(1, 6):
    print(i)
# while loop
w = 3
while w < 5:
    print(w)
    w += 1

# Jump Statements:
# break:
for i in range(1, 10):
    if i == 5:
        break
    print(i)
# continue
for i in range(1, 10):
    if i == 3:
        continue
    print(i)
# pass
for i in range(1, 10):
    if i == 3:
        pass
    else:
        print(i)

# Functions in Python:

firstName = "Arun"
lastName = "Kumar"
def name():
    print(firstName, lastName)

name()

def addition(a, b):
    print(a + b)

addition(100, 100)

age = 20
def func():
    return age

res = func()
print("The result is:", res)

# Inbuilt Functions in Python
# String Functions
my_string = "Hello, World!"
print(len(my_string))
print(my_string.lower())
print(my_string.upper())
print(my_string.replace("World", "coders"))

# list functions:
# append():
a = [1, 2, 3]
a.append(4)
print(a)

# count():
b = [1, 2, 3, 4, 5, 6, 7, 2, 3, 2, 5, 3 , 7, 2]
print(b.count(3))