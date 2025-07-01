# Functions : It is block of statements that perform a specific task.
# Advantages of using functions:
# 1. Code reusability: You can use the same function multiple times without rewriting the code.
# 2. Modularity: Functions help in breaking down complex problems into smaller, manageable parts
# 3. Readability: Functions make the code more organized and easier to understand.
# 4. Testing: Functions can be tested independently, making debugging easier.
# 5. Maintainability: Changes can be made to a function without affecting the rest of the codebase.
# Functions also used to reduce the redundancy of code.
# syntax:
#  def function_name(param1,param2, ...):  // function defination
#     # some work
#     return value  # optional
# function_name(arg1, arg2, ...) // function call


def cal_sum(a, b): # function definition
   return a + b

sum = cal_sum(10, 29) #fucntion call
# print(sum)



def print_hello():
    print("Hello, World!")
    
# print_hello()

# Average oof three numbers

def average(num1, num2, num3):
     print((num1+num2+num3)/3)

# average(50, 60, 170)


# Functions in Python
# 1)  Built-in functions : 1) print(), 2) len(), 3) type(), 4) range()
# print("hello world") # built-in function
# print("Ankit Bhagat","Hello Python") # end = "\n"
# print("Ankit Bhagat", end=" ")
# print("Python ready")


# 2) User-defined functions : The functions which are written by the user are called user-defined functions.



# Default parameters in fucntions
# Assigning a default value to parameter , which is used when no argument is passed

def cal_product(a, b=2): # default value of a and b is 1  ## b is default parameter and a is non-default parameter
    print(a * b)
    return a * b
# cal_product(1)


# Practice Questions

# WAF to print the length of a List.(list is the parameter)

cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
heros = ["spiderman", "batman", "superman", "ironman", "hulk"]
def print_length(list):
    print(len(list))
    
# print_length(cities)
# print_length(heros)
# print_length(cities)

# WAF to print the elements of a list in a single line.(list is the parameter)

def print_list(list):
    for item in list:
        print(item, end=" ")
# print_list(heros)

# WAF to find the factorial of n.(n is the parameter)

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        # fact = fact * i
        fact *= i
    print(fact)
    
# factorial(5)

# WAF to convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR" )
    
# converter(100)

# odd string and even string and take input as number
def odd_even_string(n):
    if n %2 == 0:
        print("Even String")
    else:
        print("Odd String")

odd_even_string(5)
odd_even_string(10)