# 1] program to  print Hello World
print("Hello World")

# 2] program to find the largest of three numbers

a = 10
b = 20
c = 30

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


# 3] sum of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)

# 4] program to determine whether a number is even or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# 5] Basic calculator program
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

print("The result is:", result)

# 6] proogram to check the number is positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print(f"{num} is zero.")


# 7] program to find sum of all digits of a number
num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10
print("The sum of all digits is:", sum_of_digits)


# 8] Program to find the factorial of a number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("The factorial of", num, "is:", factorial)

#9] Program to check if a number is prime or not
num = int(input("Enter a number: "))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


#10] Accept 5 numbers from user and display their cubes
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

for num in numbers:
    print(f"The cube of {num} is {num ** 3}")

#11] program to reverse a number

num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num //= 10

print("The reversed number is:", reversed_num)

#12] To determine whether a given year is a leap year or not

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")

else:
    print(f"{year} is not a leap year.")

# 13] program to give grade based on marks
marks = int(input("Enter marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"

elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"The grade is: {grade}")

#14] print student details
print("Student Name: Shritej")
print("Address: Pune")
print("Contact_No: 9876543210")
print("Mother Tongue: Marathi")
print("School_Name: ABC School")
print("Year: 2026")
print("Panel: A")
print("Roll_No: 25")

#15] multiline comment


"""
print("Address: Pune")
print("Contact_No: 9876543210")
print("Mother Tongue: Marathi")
"""

print("School_Name: ABC School")
print("Year: 2026")
print("Panel: A")
print("Roll_No: 25")

#16]. Accept Student  Name, Roll Number and Marks of the 3 subjects from the user. 
# Calculate the percentage of the marks and display it. Display the Subject with Highest and lowest marks. 
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

maths = float(input("Enter Mathematics marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

total = maths + physics + chemistry
percentage = total / 3

print("\nStudent Name:", name)
print("Roll Number:", roll_no)
print("Percentage:", percentage, "%")

if maths >= physics and maths >= chemistry:
    print("Highest marks: Mathematics =", maths)
elif physics >= maths and physics >= chemistry:
    print("Highest marks: Physics =", physics)
else:
    print("Highest marks: Chemistry =", chemistry)

if maths <= physics and maths <= chemistry:
    print("Lowest marks: Mathematics =", maths)
elif physics <= maths and physics <= chemistry:
    print("Lowest marks: Physics =", physics)
else:
    print("Lowest marks: Chemistry =", chemistry)



# LIST OPERATIONS
#1] program to access elements of a list
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Third element:", numbers[2])
print("Fourth element:", numbers[3])
print("Fifth element:", numbers[4])

#2] program to append an element to a list

numbers = [10, 20, 30, 40, 50]

numbers.append(60)

print("List after appending:", numbers)


#3] program to reverse a list
numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print("Reversed list:", numbers)


#4] program to count occurrences of an element in a list
numbers = [10, 20, 10, 30, 10, 40, 20]

element = int(input("Enter element to count: "))

count = numbers.count(element)

print("Number of occurrences:", count)

#5] program to concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list2 = list1 + list2

print("Final list:", list2)

#6] program to insert an element at a specific position in a list
numbers = [10, 20, 30, 40, 50]

numbers.insert(1, 15)

print("List after insertion:", numbers)


#7] program to remove an element at a specific index from a list
numbers = [10, 20, 30, 40, 50]

index = int(input("Enter index to remove: "))

numbers.pop(index)

print("List after removal:", numbers)

#8]  program to remove an element from a list by value
numbers = [10, 20, 30, 20, 40, 50]

element = int(input("Enter element to remove: "))

if element in numbers:
    numbers.remove(element)
    print("List after removal:", numbers)
else:
    print("Element not found")


#9] program to analyze a list of numbers
numbers = []

for i in range(20):
    num = int(input("Enter number: "))
    numbers.append(num)

print("\nList:", numbers)

# a) Similar elements and their indexes
print("\nSimilar elements and their indexes:")

for num in set(numbers):
    indexes = []

    for i in range(len(numbers)):
        if numbers[i] == num:
            indexes.append(i)

    if len(indexes) > 1:
        print(num, "occurs", len(indexes), "times at indexes", indexes)

# b) Count even and odd
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("\nEven numbers:", even)
print("Odd numbers:", odd)

# c) Count positive and negative
positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)

#10] program to sort a list of numbers
numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

# a) Ascending using sorted()
ascending = sorted(numbers)

print("Ascending order:", ascending)

# b) Descending using sort()
numbers.sort(reverse=True)

print("Descending order:", numbers)

# c) Length of list
print("Length of list:", len(numbers))


#11] program to merge two lists
list1 = []
list2 = []

n1 = int(input("Enter number of elements in list 1: "))

for i in range(n1):
    list1.append(int(input("Enter element: ")))

n2 = int(input("Enter number of elements in list 2: "))

for i in range(n2):
    list2.append(int(input("Enter element: ")))

merged_list = list1 + list2

print("List 1:", list1)
print("List 2:", list2)
print("Merged list:", merged_list)


#12] program to create an acronym from a phrase
phrase = input("Enter a phrase: ")

words = phrase.split()

acronym = ""

for word in words:
    acronym = acronym + word[0]

print("Acronym:", acronym.upper())

#13] program to get month abbreviation
month = int(input("Enter month number: "))

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

if month >= 1 and month <= 12:
    print("Month abbreviation:", months[month - 1])
else:
    print("Invalid month number")


#14] program to insert and delete elements in a list
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# Insert
numbers.insert(2, 25)
print("After insertion:", numbers)

# Delete
numbers.remove(40)
print("After deletion:", numbers)

# Display
print("Final list:", numbers)



#15] program to create a dictionary from two lists
keys = ["Name", "Age", "Branch"]
values = ["Shritej", 18, "AI-DS"]

student = dict(zip(keys, values))

print("Dictionary:", student)

#16] program to remove duplicates from a list
numbers = [10, 20, 10, 30, 20, 40, 30]

unique_numbers = list(set(numbers))

print("Original list:", numbers)
print("List after removing duplicates:", unique_numbers)

#17] program to create a dictionary from two lists
keys = ["Name", "Roll No", "Branch"]

values = ["Shritej", 25, "AI-DS"]

student = dict(zip(keys, values))

print("Dictionary:", student)

#18] program to find common elements in two lists
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for num in list1:
    if num in list2:
        common.append(num)

print("Common elements:", common)


#  DICTIONARY OPERATIONS

#1] Inserting an element into a dictionary
my_dict = {0: 10, 1: 20}

my_dict[2] = 30

print("Dictionary:", my_dict)

#2] Merging dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict = {}

new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print("New Dictionary:", new_dict)

#3]check whether the dictionary exists or not
my_dict = {
    101: "Amit",
    102: "Rahul",
    103: "Priya"
}

key = int(input("Enter key to search: "))

if key in my_dict:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")


#4] Displaying keys, values, and key-value pairs
my_dict = {
    101: "Amit",
    102: "Rahul",
    103: "Priya"
}

print("Keys:")

for key in my_dict:
    print(key)

print("\nValues:")

for value in my_dict.values():
    print(value)

print("\nKeys and Values:")

for key, value in my_dict.items():

    print(key, value)


#5] Creating a dictionary with squares of numbers from 1 to 15
my_dict = {}

for i in range(1, 16):
    my_dict[i] = i ** 2

print(my_dict)


#6]
my_dict = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

total = 0

for value in my_dict.values():
    total = total + value

print("Sum of values:", total)



#7] Managing student information in a dictionary
my_dict = {
    101: "Amit",
    102: "Rahul",
    103: "Priya",
    104: "Sneha",
    105: "Neha"
}

print("Original Student Information:")
print(my_dict)

# Add student
my_dict[106] = "Rohan"

print("\nAfter Adding Student:")
print(my_dict)

# Delete student
del my_dict[103]

print("\nAfter Deleting Student:")
print(my_dict)

# Display student information
print("\nStudent Information:")

for roll_no, name in my_dict.items():
    print("Roll No:", roll_no, "Name:", name)



#8] Creating a dictionary from two lists
list1 = ["name", "panel", "rollno"]
list2 = ["ABC", "B", 34]

my_dict = dict(zip(list1, list2))

print("Dictionary:", my_dict)


#9] Converting dictionary to lists
my_dict = {
    "name": "ABC",
    "panel": "B",
    "rollno": 34
}

keys_list = list(my_dict.keys())
values_list = list(my_dict.values())

print("Keys List:", keys_list)
print("Values List:", values_list)


#10] Calculating mean of dictionary values
mydict = {
    "marks1": 23,
    "marks2": 123,
    "marks3": 43,
    "marks4": 13,
    "marks5": 39
}

total = sum(mydict.values())

mean = total / len(mydict)

print("Mean of all values:", mean)



#11] Sorting dictionary keys
my_dict = {
    "name": "ABC",
    "panel": "B",
    "rollno": 34,
    "marks": [65, 87, 67, 94]
}

sorted_dict = sorted(my_dict)

print("Sorted keys:", sorted_dict)


#12] Finding the student with the highest marks
students = {
    "Amit": 85,
    "Rahul": 92,
    "Priya": 78,
    "Sneha": 95,
    "Neha": 88
}

highest_student = max(students, key=students.get)

print("Student with highest marks:", highest_student)
print("Highest Marks:", students[highest_student])


#13] Finding frequency of elements in a list
numbers = [10, 20, 10, 30, 20, 10, 40, 30]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1

print("Frequency of elements:", frequency)


#14] Sorting dictionary by values
my_dict = {
    "Amit": 85,
    "Rahul": 72,
    "Priya": 95,
    "Sneha": 80
}

sorted_dict = dict(
    sorted(my_dict.items(), key=lambda item: item[1])
)

print("Dictionary sorted by values:")
print(sorted_dict)


# TUPLE OPERATIONS

#1] program to access elements of a tuple
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90)

print("Tuple:", numbers)

print("4th element from first:", numbers[3])

print("4th element from last:", numbers[-4])


#2] program to search for an element in a tuple
numbers = (10, 20, 30, 40, 50)

element = int(input("Enter element to search: "))

if element in numbers:
    print("Element exists in the tuple")
else:
    print("Element does not exist in the tuple")



#3] converting a list to a tuple
numbers_list = [10, 20, 30, 40, 50]

numbers_tuple = tuple(numbers_list)

print("List:", numbers_list)
print("Tuple:", numbers_tuple)


#4] program to find the index of an element in a tuple
numbers = (10, 20, 30, 40, 50)

element = int(input("Enter element: "))

if element in numbers:
    print("Index of element:", numbers.index(element))
else:
    print("Element not found")


#5] program to modify elements in a tuple
numbers = [
    (10, 20, 40),
    (40, 50, 60),
    (70, 80, 90)
]

new_list = []

for tup in numbers:
    new_tup = tup[:-1] + (100,)
    new_list.append(new_tup)

print("Original List:", numbers)
print("Updated List:", new_list)



#6] program to find maximum and minimum elements in a tuple
numbers = (25, 10, 45, 5, 60, 30)

maximum = max(numbers)
minimum = min(numbers)

print("Tuple:", numbers)
print("Maximum element:", maximum)
print("Minimum element:", minimum)



#7] program to swap first and last elements in a tuple
numbers = (10, 20, 30, 40, 50)

new_tuple = (numbers[-1],) + numbers[1:-1] + (numbers[0],)

print("Original Tuple:", numbers)
print("Tuple after swapping:", new_tuple)

