'''Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.'''
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} / {b} is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

'''Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.'''
def get_integer_input():
    try:
        user_input = input("Please enter an integer: ")
        value = int(user_input)
        print(f"You entered the integer: {value}")
    except ValueError:
        print("Error: That is not a valid integer.")

'''Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.'''
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

'''Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.'''
def get_two_numbers():
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        # Attempt to convert inputs to floats
        num1 = float(num1)
        num2 = float(num2)
        
        print(f"You entered {num1} and {num2}")
    except ValueError:
        raise TypeError("Error: Both inputs must be numerical.")


'''Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.'''
def open_file_with_permission_check(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except PermissionError:
        print(f"Error: Permission denied when trying to open '{file_path}'.")

'''Write a Python program that executes an operation on a list and handles an 
IndexError exception if the index is out of range.'''
def access_list_element(lst, index):
    try:
        element = lst[index]
        print(f"The element at index {index} is {element}")
    except IndexError:
        print(f"Error: Index {index} is out of range.")

'''Write a Python program that prompts the user to input a number and handles 
a KeyboardInterrupt exception if the user cancels the input.'''
def get_number_input():
    try:
        user_input = input("Please enter a number: ")
        value = float(user_input)
        print(f"You entered the number: {value}")
    except KeyboardInterrupt:
        print("\nError: Input was cancelled by the user.")

'''Write a Python program that executes division and handles an ArithmeticError 
exception if there is an arithmetic error.'''
def safe_division(a, b):
    try:
        result = a / b
        print(f"The result of {a} / {b} is {result}")
    except ArithmeticError:
        print("Error: An arithmetic error occurred.")

'''Write a Python program that opens a file and handles a UnicodeDecodeError 
exception if there is an encoding issue.'''
def read_file_with_encoding(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except UnicodeDecodeError:
        print(f"Error: Unicode decode error occurred while reading '{file_path}'.")

'''Write a Python program that executes a list operation and handles an AttributeError 
exception if the attribute does not exist.'''
def list_operation(lst):
    try:
        lst.append(4)
        print(f"List after append operation: {lst}")
        
        lst.non_existent_method()
    except AttributeError:
        print("Error: The list object does not have the attribute 'non_existent_method'.")

list_operation([1, 2, 3])

