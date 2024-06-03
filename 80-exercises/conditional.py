'''Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).'''
result = [num for num in range(1500, 2701) if num % 7 == 0 and num % 5 == 0]
print("Result:", result)

'''Write a Python program to convert temperatures to and from Celsius and Fahrenheit.'''
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_temp = 60
fahrenheit_temp = 45
print(f"{celsius_temp}°C is {celsius_to_fahrenheit(celsius_temp)} in Fahrenheit")
print(f"{fahrenheit_temp}°F is {fahrenheit_to_celsius(fahrenheit_temp)} in Celsius")

'''Write a Python program to guess a number between 1 and 9.'''
import random

def guess_number():
    target = random.randint(1, 9)
    while True:
        guess = int(input("Guess a number between 1 and 9: "))
        if guess == target:
            print("Well guessed!")
            break

guess_number()

'''Write a Python program to construct the following pattern, using a nested for loop.'''
for i in range(5):
    print("* " * (i + 1))
for i in range(4, 0, -1):
    print("* " * i)

'''Write a Python program that accepts a word from the user and reverses it.'''
word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

'''Write a Python program to count the number of even and odd numbers in a series of numbers.'''
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = sum(1 for num in numbers if num % 2 != 0)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

'''Write a Python program that prints each item and its corresponding type from the following list.'''
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for item in datalist:
    print(f"Item: {item}, Type: {type(item)}")

'''Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.'''
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i, end=" ")

'''Write a Python program to get the Fibonacci series between 0 and 50.'''
a, b = 0, 1
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b

'''Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz", for multiples of five print "Buzz", and for numbers that are multiples of both three and five, print "FizzBuzz".'''
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

'''Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.'''
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
result = [[i * j for j in range(n)] for i in range(m)]
print("Result:", result)

'''Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).'''
print("Enter lines (terminate with blank line):")
lines = []
while True:
    line = input().strip()
    if not line:
        break
    lines.append(line.lower())
for line in lines:
    print(line)

'''Write a Python program that accepts a sequence of comma-separated 4-digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma-separated sequence.'''
binary_numbers = input("Enter comma-separated 4-digit binary numbers: ").split(',')
result = [num for num in binary_numbers if int(num, 2) % 5 == 0]
print("Result:", ','.join(result))

'''Write a Python program that accepts a string and calculates the number of digits and letters.'''
string = input("Enter a string: ")
letters = sum(1 for char in string if char.isalpha())
digits = sum(1 for char in string if char.isdigit())
print("Letters:", letters)
print("Digits:", digits)

'''Write a Python program to check the validity of passwords input by users.'''
import re
password = input("Enter a password: ")
if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$#]{6,16}$", password):
    print("Valid password")
else:
    print("Invalid password")

'''Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.'''
result = [str(num) for num in range(100, 401) if all(int(digit) % 2 == 0 for digit in str(num))]
print("Result:", ','.join(result))

'''Write a Python program to print the alphabet pattern 'A'.'''
for i in range(7):
    if i == 0:
        print(" *** ")
    elif i == 3:
        print("*****")
    else:
        print("*   *")


'''Write a Python program to print the alphabet pattern 'D'.'''
for i in range(7):
    if i == 0 or i == 6:
        print("**** ")
    else:
        print("*   *")

'''Write a Python program to print the alphabet pattern 'E'.'''
for i in range(7):
    if i == 0 or i == 3 or i == 6:
        print("*****")
    else:
        print("*")

'''Write a Python program to print the alphabet pattern 'G'.'''
result_str = ""

for row in range(0, 7):
    for column in range(0, 7):
        
        if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "

    result_str = result_str + "\n"

print(result_str) 

