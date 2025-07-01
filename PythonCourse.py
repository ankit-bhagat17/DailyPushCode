# .py is extension for Python files


# print() is a function that outputs text to the console
# The text inside the parentheses is called a string
# Strings are enclosed in quotes, either single or double

print("Hello World!")
 
# 1) Variables : It is a container for storing data values.
# Variables are created when you assign a value to them.
# Variable names can contain letters, numbers, and underscores, but cannot start with a number.
# Variable names are case-sensitive, meaning that "myVariable" and "myvariable" are different variables.

name = "Ankit"
age = 21

# print("My name is", name, "and I am", age, "years old.")

# We can change the value of a variable at any time

name = "Shourya"
age = 6
print("My name is", name, "and I am", age, "years old.")

# 2) There are different types of variables in Python:
# 1) String: A string is a sequence of characters enclosed in quotes.
# 2) Integer: An integer is a whole number, positive or negative, without decimals
# 3) Float: A float is a number that has a decimal point.
# 4) Boolean: A boolean is a data type that can be either True or False
# 5) List: A list is a collection of items that can be of different types, enclosed in square brackets.
# 6) Tuple: A tuple is similar to a list, but it is immutable (cannot be changed), enclosed in parentheses.
# 7) Dictionary: A dictionary is a collection of key-value pairs, enclosed in curly braces.
# 8) Set: A set is a collection of unique items, enclosed in curly braces.
# 9) None: None is a special type that represents the absence of a value or a null value.

#  Example of different types of variables
string_var = "Hello, World!"  # String
integer_var = 42              # Integer
float_var = 3.14              # Float
boolean_var = True             # Boolean
list_var = [1, 2, 3, "Python"]  # List
tuple_var = (1, 2, 3)          # Tuple
dict_var = {"name": "Alice", "age": 30}  # Dictionary
set_var = {1, 2, 3}            # Set
none_var = None                # None    

# User Input by using input() function 
# It is used to tkae the input from the user
user_name = input("What is your name? ")
user_age = input("Enter your age: ")
print("My name is", user_name, "and I am ", user_age, "years old.")


# 3) Type Conversion : It is the process of converting one data type to another.
# Python automatically converts data types when necessary, but you can also explicitly convert them using functions like
# int(), float(), str(), etc.   
# Example of type conversion
num_str = "123"  # String
num_int = int(num_str)  # Convert string to integer
num_float = float(num_str)  # Convert string to float
print("String:", num_str, "Integer:", num_int, "Float:", num_float)

old_age = input("Enter your old age: ")
new_age = int(old_age) + 2
print(new_age)

number = 18
print(float(number))  # Convert integer to float
print(str(number))    # Convert integer to string


# Write a program that takes two numbers as input from the user, and then prints their Sum.

First = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
Sum = First + second
print("The sum of two numbers is: ",+Sum)

# 4) Strings : It is a sequence of characters enclosed with single or double quotes.
# There are many built-in methods in Python to manipulate strings.
# Some common string methods include:
# 1) upper() : Converts all characters in a string to uppercase.
# 2) lower() : Converts all characters in a string to lowercase.
# 3) strip() : Removes leading and trailing whitespace from a string.
# 4) replace(old, new) : Replaces occurrences of a substring with another substring.
# 5) split(separator) : Splits a string into a list of substrings based on a separator.
# 6) join(iterable) : Joins elements of an iterable (like a list) into a single string with a specified separator.
# 7) find(substring) : Returns the index of the first occurrence of a substring in a string, or -1 if not found.
# 8) count(substring) : Returns the number of occurrences of a substring
# 9) title() : Converts the first character of each word to uppercase and the rest to lowercase.
# 10) isdigit() : Checks if all characters in a string are digits 
# 11) isalpha() : Checks if all characters in a string are alphabetic (letters only).
# 12) isalnum() : Checks if all characters in a string are alphanumeric (letters and numbers).

name = "Tony Stark"
print(name.upper())  # Convert string to uppercase
print(name.lower()) # Convert string to lowercase
print(name.find("S"))  # Find the index of a substring and returns the index of the first occurrence

# index means the position of a character in a string, starting from 0 it also includes spaces
print(name.replace("Tony Stark", "Ironman"))  # Replace a substring with another substring
print(name)

print("T" in name) # Check if a character is present in the string if it is present it will return True otherwise False
print("Stark" in name) 

# 5) Arithmetic Operators : These are used to perform mathematical operations on numbers.
# 1) Addition (+)
# 2) Subtraction (-)
# 3) Multiplication (*)
# 4) Division (/)
# 5) Modulus (%) : Returns the remainder of a division operation.
# 6) Exponentiation (**): Raises a number to the power of another number.
# 7) Floor Division (//): Returns the largest integer less than or equal to the

a =  10
b = 5
print("Addition of", a, "and", b, "is:", a+b)
print("Subtraction of", a, "and", b, "is:", a-b)
print("Multiplication of", a, "and", b, "is:", a*b)
print("Division of", a, "and", b, "is:", a/b)
print("Modulus(Ramender) of", a, "and", b, "is:", a%b)
print("floor Division of", a, "and", b, "is:", a//b)
print("Exponentiation of", a, "and", b, "is:", a**b)


# 6) Operator Precedence : It determines the order in which operators are evaluated in an expression.
# The order of precedence is as follows:
# 1) Parentheses ()
# 2) Exponentiation (**)
# 3) Multiplication (*), Division (/), Modulus (%)
# 4) Addition (+), Subtraction (-)  

result = 2 + 3 * 5
print(result)

# Comments : It is unused lines in the code that are not executed.
# They are used to explain the code and make it more readable.
# Single-line comments start with a hash (#) symbol.
# Multi-line comments can be created using triple quotes (''' or """) or by using multiple  

# 7) Comparison Operators : These are used to compare two values and return a boolean result (True or False).
# 1) Equal to (==)
# 2) Not equal to (!=)
# 3) Greater than (>)
# 4) Less than (<)
# 5) Greater than or equal to (>=)
# 6) Less than or equal to (<=)

print(3>1)
print(3<1)
print(3==1)
print(3!=1)
print(3>=1)
print(3<=1)

# 8) Logical Operators : These are used to combine multiple conditions and return a boolean result.
# 1) and : Returns True if both conditions are True.
# 2) or : Returns True if at least one condition is True.   
# 3) not : Returns True if the condition is False, and vice versa.

print(3 > 1 and 2 < 5)  # True, both conditions are True
print(3 < 1 or 2 < 5)   # True, at least one condition is True
print(not (3 > 1))       # False, negates the condition

# if-else statements : These are used to make decisions in the code based on conditions.
# if condition:
#     # code to execute if condition is True
# else:
#     # code to execute if condition is False   

# Example of if-else statement 
age = int(input("Enter Your Age: "))
if(age>= 18):
    print("Congratulations, you are eligible to vote.")
else:
    print("Sorry, you are not eligible to vote yet.")
    


# Mini Project Calculator

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
operation = input("Enter the operation(+,-,*,/,%): ")

if operation == "+":
    print(first + second)
elif operation == "-":
    print(first - second)
elif operation =="*":
    print(first*second)
elif operation == "/":
    print(first / second)
elif operation =="%":
    print(first % second)
else:
    print("Invalid Operation")
 
# 9) Range : It is a built-in function that generates a sequence of numbers.
r = range(0,5)  # Generates numbers from 0 to 4
print(r)

# 10) Loops : These are used to repeat a block of code multiple times.
# 1) for loop : Used to iterate over a sequence (like a list, tuple, or string) or a range of numbers.
# 2) while loop : Used to repeat a block of code as long as a condition is True.
# Example of while loop
i = 1
while i <= 100:
    print(i)
    i = i + 1

i = 1
while i <= 5:
    print(i * "*")
    i = i + 1

i = 5
while i >= 0:
    print(i * "*")
    i = i - 1

# Example of for loop

for i in range(5):
    print(i)


# 11) List : It is a collection of items that can be of different types, enclosed in square brackets.
# Lists are mutable, meaning you can change their contents after creation.
# You can access list items using their index, which starts from 0.

# Example of a list
marks = [55, 87, 90]
print(marks[0])  # Accessing the first item in the list
print(marks[-1])  # Accessing the last item in the list
print(marks[0:2]) # Accessing a range of items in the list (from index 0 to 1)

for score in marks:
    print(score)

# List methods/operations:
# 1) append(item) : Adds an item to the end of the list.
# 2) insert(index, item) : Inserts an item at a specific index in the
# list.
# 3) remove(item) : Removes the first occurrence of an item from the list.
# 4) pop(index) : Removes and returns the item at the specified index (default is the last item).
# 5) sort() : Sorts the items in the list in ascending order.
# 6) reverse() : Reverses the order of items in the list.
# 7) extend(iterable) : Adds all items from an iterable (like another list) to the end of the list.
# 8) count(item) : Returns the number of occurrences of an item in the list.
# 9) index(item) : Returns the index of the first occurrence of an item in the list.
# 10) clear() : Removes all items from the list.    

# Example of list methods
marks.append(100) # Adds 100 to the end of the list
print(marks)

marks.insert(1, 99)
print(marks)  # Inserts 99 at index 1

marks.remove(55)  # Removes the first occurrence of 55 from the list
print(marks)

marks.pop(1)  # Removes and returns the item at index 1
print(marks)

marks.sort()
print(marks)  # Sorts the list in ascending order

marks.reverse() # Reverses the order of items in the list
print(marks)

print(marks.count(90)) # Returns the number of occurrences of 90 in the list

print(marks.index(55)) # Returns the index of the first occurrence of 55 in the list

marks.clear()  # Removes all items from the list
print(marks)  # Prints an empty list
print(len(marks)) # Returns the number of items in the list

# Iterate over a list using a while loop 

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

# 12) Break and Continue 

students = ["Ankit", "Shourya", "Aman", "Radha", "Chaitu"]

for student in students:
    if student == "Radha":
        break
    print(student)

for student in students:
    if student == "Shourya":
        continue
    print(student)

# 13) Tuple : It is similar to a list, but it is immutable (cannot be changed), enclosed in parentheses.
# Tuples are used to store multiple items in a single variable.

marks = (95, 98, 97)
print(marks.index(98))  # Returns the index of the first occurrence of 98 in the tuple

# 14) Sets: It is a collection of unique items, enclosed in curly braces.
# Sets are unordered, meaning the items do not have a specific order.

marks = {95, 98, 97, 95}  # Duplicate value will be removed
print(marks)  # Prints the set with unique items


# 15) Dictionary: It is a collection of key-value pairs, enclosed in curly braces.
# Dictionaries are used to store data in a key-value format, where each key is unique.

person = { "name": "Ankit", "age": 21, "city": "Nagpur"}
print(person["name"])  # Accessing the value associated with the key "name"
person["age"] = 23 # Updating the value associated with the key "age"
print(person)
# List - [], Tuple - (), Set - {}, Dictionary - {}

# 16) Functions: Functions are reusable blocks of code that perform a specific task.
# They can take input parameters and return a value.        
# 1) In-built Functions: These are functions that are already defined in Python, such as print(), input(), len(), etc.
# 2) User-defined Functions: These are functions that you define yourself to perform specific tasks.
# 3) Module Functions: These are functions that are defined in external modules or libraries that you can import and use in your code.


# from math import sqrt  # Importing the math module to use its functions
# print(sqrt(144))

# User-defined function example

# def print_sum(x, y=99):
#     print(x + y)

# print_sum(19)