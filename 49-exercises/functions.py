'''Write a Python function to find the maximum of three numbers.'''
def max_of_three(a, b, c):
    return max(a, b, c)

print("Max of 3, 6, -5:", max_of_three(3, 6, -5))

'''Write a Python function to sum all the numbers in a list.'''
def sum_list(numbers):
    return sum(numbers)

sample_list = [8, 2, 3, 0, 7]
print("Sum of the list:", sum_list(sample_list))

'''Write a Python function to multiply all the numbers in a list.'''
def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

sample_list = [8, 2, 3, -1, 7]
print("Product of the list:", multiply_list(sample_list))

'''Write a Python program to reverse a string.'''
def reverse_string(s):
    return s[::-1]

sample_string = "1234abcd"
print("Reversed string:", reverse_string(sample_string))

'''Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5))

'''Write a Python function to check whether a number falls within a given range.'''
def is_in_range(n, start, end):
    return start <= n <= end

print("Is 5 in range 1-10:", is_in_range(5, 1, 10))

'''Write a Python function that accepts a string and counts the number of upper and lower case letters.'''
def count_upper_lower(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

sample_string = 'The quick Brow Fox'
upper, lower = count_upper_lower(sample_string)
print("No. of Upper case characters :", upper)
print("No. of Lower case Characters :", lower)

'''Write a Python function that takes a list and returns a new list with distinct elements from the first list.'''
def unique_elements(lst):
    return list(set(lst))

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
print("Unique list:", unique_elements(sample_list))

'''Write a Python function that takes a number as a parameter and checks whether the number is prime or not.'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 7 prime:", is_prime(7))

'''Write a Python program to print the even numbers from a given list.'''
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Even numbers:", even_numbers(sample_list))

'''Write a Python function to check whether a number is "Perfect" or not.'''
def is_perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

print("Is 6 a perfect number:", is_perfect_number(6))
print("Is 28 a perfect number:", is_perfect_number(28))

'''Write a Python function that checks whether a passed string is a palindrome or not.'''
def is_palindrome(s):
    return s == s[::-1]

print("Is 'madam' a palindrome:", is_palindrome("madam"))
print("Is 'hello' a palindrome:", is_palindrome("hello"))

'''Write a Python function that prints out the first n rows of Pascal's triangle.'''
def pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)
    return triangle

for row in pascals_triangle(5):
    print(row)

'''Write a Python function to check whether a string is a pangram or not.'''
def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(s.lower())

print("Is 'The quick brown fox jumps over the lazy dog' a pangram:", is_pangram("The quick brown fox jumps over the lazy dog"))

'''Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.'''
def sort_hyphenated_words(s):
    words = s.split('-')
    words.sort()
    return '-'.join(words)

sample_words = "green-red-yellow-black-white"
print("Sorted hyphen-separated words:", sort_hyphenated_words(sample_words))

'''Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).'''
def squares_list():
    return [i**2 for i in range(1, 31)]

print("Squares of numbers from 1 to 30:", squares_list())

'''Write a Python program to create a chain of function decorators (bold, italic, underline etc.).'''
def bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped

@bold
@italic
@underline
def decorated_text():
    return "Hello, World!"

print(decorated_text())

'''Write a Python program to execute a string containing Python code.'''
def execute_code(code):
    exec(code)

code = 'print("Hello from executed code!")'
execute_code(code)

'''Write a Python program to access a function inside a function.'''
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

inner = outer_function(5)
print("Result of inner function:", inner(10))

'''Write a Python program to detect the number of local variables declared in a function.'''
def local_variables_count():
    a = 1
    b = 2
    c = 3
    return locals()

print("Number of local variables:", len(local_variables_count()))

'''Write a Python program that invokes a function after a specified period of time.'''
import time

def delayed_function_call(func, delay, *args):
    time.sleep(delay)
    return func(*args)

print("Square root after delay:", delayed_function_call(lambda x: x**0.5, 2, 16))
