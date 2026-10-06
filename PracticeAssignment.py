#Python Basics- Practice assignment

print("Student Name:")
"""
print("Address")
print("Contact Number")
print("Mother Tongue")
"""
print("School Name")
print("Year")
print("Panel")
print('Roll No:')

#3
name = input("Student Name: ")
roll = input("Roll No: ")
m1 = float(input("Marks of Subject 1: "))
m2 = float(input("Marks of Subject 2: "))
m3 = float(input("Marks of Subject 3: "))

marks = {"Subject 1": m1, "Subject 2": m2, "Subject 3": m3}
total = m1 + m2 + m3
percentage = total / 3

highest = max(marks, key=marks.get)
lowest = min(marks, key=marks.get)
#4
num =90
if num<0:
    print('The number is negative')

elif num==0:
    print("The number is zero")

else:
    print("The number is positive")

#5
if num % 2 == 0:
    print("The number is even")

else:
    print("The number is odd")

#6
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1%10 == num2%10:
    print("The last digits are the same.")

else:
    print("The last digits are different.")


#7
for i in range(1, 11):
    print(i, end=' ')

#8
for i in range (23,57):
    if i%2==0:
        print(i, end=' ')


#9
n = int(input("Enter number: "))
if n < 2:
    print("Not Prime")
else:
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    print("Prime" if prime else "Not Prime")


#10
for n in range(10, 100):
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    if prime:
        print(n)

#11
n = abs(int(input("Enter number: ")))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits:", total)

#12
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))

#14
# Loop 5 times to get 5 numbers from the user
for i in range(5):
    # Accept input and convert it to a float to support decimals
    number = float(input(f"Enter number {i + 1}: "))
    
    # Calculate the cube using the exponent operator (**)
    cube = number ** 3
    
    # Display the result
    print(f"The cube of {number} is {cube}\n")





#LIST
#1
l1 = [1, 2, 3, 4, 5]
print("List:", l1)

print(l1[0])  
print(l1[-1])  

#2
print(l1.append(6))

#3
print(l1[::-1])

#4
print(len(l1))

#5
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result_list = list1 + list2

print("Combined List:", result_list)
# Output: [1, 2, 3, 4, 5, 6]

#6

print(l1.insert(1,10))

#7
print(l1.remove(3))

#8
print(l1.pop(0))

#9

numbers = []
for i in range(20):
    numbers.append(int(input(f"Enter value {i+1}: ")))

print("Similar elements and their indexes:")
for x in dict.fromkeys(numbers):
    indexes = [i for i, v in enumerate(numbers) if v == x]
    if len(indexes) > 1:
        print(x, "count =", len(indexes), "indexes =", indexes)

even = sum(1 for x in numbers if x % 2 == 0)
odd = len(numbers) - even
positive = sum(1 for x in numbers if x > 0)
negative = sum(1 for x in numbers if x < 0)

print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)


#10
numbers = [int(input(f"Enter value {i+1}: ")) for i in range(10)]

print("Ascending:", sorted(numbers))
numbers.sort(reverse=True)
print("Descending:", numbers)
print("Length:", len(numbers))

#11
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = list1 +list2
print(list3)


#TUPLE
1
t1 = (1, 2, 3, 4, 5)
print("Tuple:", t1)

print(t1[3])
print(t1[-4])

#2
x  = int(input("Enter a number: "))

if x in t1:
    print("The number is present in the tuple.")

else:
    print("The number is not present in the tuple.")

#3
list = [1, 2, 3, 4, 5]

print(tuple(list))  

#4
t2= (19, 25, 32, 45,65)

n = int(input("Enter a number: "))

if n in t2:
    print("Index :", t2.index(n))

else:
    print("The number is not present in the tuple.")

#5
#DOUBT

#SETS OPERATIONS
#1
S = {1, 2, 3, 4, 5}
print("Set:", S)

print(S.discard(3))
print("Set after discarding 3:", S)

#2
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Intersection:", a & b)

#3
a = {3,4,5,9,2,3}
b = {2,4,7,9,6,7}

print(a|b)

#4

print(max(a))
print(min(b))


#STRING QUESTIONS

#1
S = input("Enter a string: ")

upper = lower = 0

for ch in S:
   if ch.isupper():
       upper+=1
   elif ch.islower():
       lower+=1

print(("Uppercase Letters:",upper))

print(("Lowercase Letters:",lower))


#2
s = input("Enter a string: ")
if s ==s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#3
s = input("Enter string: ")
n = len(s)
print(s[:2] * n)


#4
s = input("Enter a string: ")

if s.startswith("x"):
    s = s[1:]

elif s.endswith("x"):
    s = s[:-1]

print("Modified string:", s)

#5
s = input("Enter string: ")
n = int(input("Enter n: "))
if n == 0:
    print("")
else:
    print(s[-n:] * n)

#REGULAR EXPRESSIONS

#1
import re

s = input("Enter string: ")
pattern = r"^[bh][aiu]t$"
if re.fullmatch(pattern, s):
    print("Valid")
else:
    print("Invalid")


import re

s = input("Enter two words: ")
pattern = r"^[A-Za-z]+ [A-Za-z]+$"
if re.fullmatch(pattern, s):
    print("Valid")
else:
    print("Invalid")
   

import re

pattern = r"^[A-Za-z]+ [A-Za-z]+$"

s = input("Enter two words: ")

if re.fullmatch(pattern, s):
    print("Valid")
else:
    print("Invalid")

import re


s = input("Enter a word and a letter :")

pattern = r"^[A-Za-z]+, [A-Za-z]$"

if re.fullmatch(pattern,s):
    print("Valid")
else:
    print("invalid")

#NUMPY 

1
import numpy as np
arr = np.ones((3, 3), dtype=bool)
print(arr)

2
import numpy as np
arr = np.linspace(5, 50, 10)
print(arr)

#3
import numpy as np
lst = [10, 20, 30, 40, 50]
arr = np.array(lst)
print(arr)

#4
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr[::-1])

#5
import numpy as np
identity = np.eye(3)
print(identity)

#6
import numpy as np
arr = np.arange(1, 17).reshape(4, 4)
print("Array:\n", arr)
print("First row:", arr[0, :])
print("Last column:", arr[:, -1])

#7
import numpy as np
arr = np.arange(1, 17).reshape(4, 4)
print("Array:\n", arr)
print("First 2 rows and columns:\n", arr[:2, :2])

#8
import numpy as np
a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#9
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Dot product:", np.dot(a, b))

#10
import numpy as np
arr = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard deviation:", np.std(arr))


#DICTIONARY OPERATIONS
#1
dict = {0: 10, 1: 20}
dict[2] = 30
print(dict)


#2
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic = {**dic1, **dic2, **dic3}
print(dic)

#3
my_dict = {"name": "ABC", "rollno": 34, "marks": 80}
key = input("Enter key: ")
if key in my_dict:
    print("Key exists")
else:
    print("Key does not exist")


4

my_dict = {"name": "ABC", "rollno": 34, "marks": 80}

print("Keys:")
for key in my_dict:
    print(key)

print("Values:")
for value in my_dict.values():
    print(value)

print("Keys and values:")
for key, value in my_dict.items():
    print(key, value)


5
squares = {i: i**2 for i in range(1, 16)}
print(squares)

#6
my_dict = {"a": 10, "b": 20, "c": 30}
total = sum(my_dict.values())
print("Sum:", total)

#7
my_dict = {
    "name": "ABC",
    "panel": "B",
    "rollno": 34,
    "branch": "AI",
    "marks": 85
}
key = input("Enter new key: ")
value = input("Enter new value: ")
my_dict[key] = value

delete_key = input("Enter key to delete: ")
my_dict.pop(delete_key, None)

print(my_dict)

#8
list1 = ["name", "panel", "rollno"]
list2 = ["ABC", "B", 34]
my_dict = dict(zip(list1, list2))
print(my_dict)

#9
my_dict = {"name": "ABC", "panel": "B", "rollno": 34}
keys = list(my_dict.keys())
values = list(my_dict.values())
print("Keys:", keys)
print("Values:", values)

#10
mydict = {"marks1": 23, "marks2": 123, "marks3": 43, "marks4": 13, "marks5": 39}
mean = sum(mydict.values()) / len(mydict)
print("Mean:", mean)

#11
my_dict = {"name": "ABC", "panel": "B", "rollno": 34, "marks": [65, 87, 67, 94]}
sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}
print(sorted_dict)



