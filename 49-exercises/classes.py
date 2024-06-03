'''Write a Python program to import a built-in array module and display the namespace of the said module.'''
import array
print("Namespace of array module:", dir(array))

'''Write a Python program to create a class and display the namespace of that class.'''
class MyClass:
    x = 5
    y = 10

print("Namespace of MyClass:", MyClass.__dict__)

'''Write a Python program to create an instance of a specified class and display the namespace of the said instance.'''
class AnotherClass:
    def __init__(self):
        self.a = 1
        self.b = 2

instance = AnotherClass()
print("Namespace of instance:", instance.__dict__)

''' 'builtins' module provides direct access to all 'built-in' identifiers of Python. 
Write a Python program that imports the abs() function using the builtins module, displays 
the documentation of the abs() function and finds the absolute value of -155.'''
import builtins
print("Documentation of abs():", builtins.abs.__doc__)
print("Absolute value of -155:", builtins.abs(-155))

'''Define a Python function student(). Using function attributes display the names of all arguments.'''
def student(name, age):
    return f"Name: {name}, Age: {age}"

print("Function student argument names:", student.__code__.co_varnames[:student.__code__.co_argcount])

'''Write a Python function student_data() that will print the ID of a student (student_id). 
If the user passes an argument student_name or student_class the function will print the student name and class.'''
def student_data(student_id, student_name=None, student_class=None):
    print(f"Student ID: {student_id}")
    if student_name:
        print(f"Student Name: {student_name}")
    if student_class:
        print(f"Student Class: {student_class}")

student_data(1)
student_data(2, student_name="John")
student_data(3, student_class="Math")

'''Write a simple Python class named Student and display its type. 
Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.'''
class Student:
    pass

print("Type of Student class:", type(Student))
print("Student class __dict__ keys:", Student.__dict__.keys())
print("Student class __module__ value:", Student.__module__)

'''Write a Python program to create two empty classes, Student and Marks.
Now create some instances and check whether they are instances of the said classes or not. 
Also, check whether the said classes are subclasses of the built-in object class or not.'''
class Student:
    pass

class Marks:
    pass

student_instance = Student()
marks_instance = Marks()

print("Is student_instance an instance of Student:", isinstance(student_instance, Student))
print("Is marks_instance an instance of Marks:", isinstance(marks_instance, Marks))
print("Is Student a subclass of object:", issubclass(Student, object))
print("Is Marks a subclass of object:", issubclass(Marks, object))

'''Write a Python class named Student with two attributes student_name, marks. 
Modify the attribute values of the said class and print the original and modified values of the said attributes.'''
class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

student = Student("Alice", 85)
print("Original values:", student.student_name, student.marks)

student.student_name = "Bob"
student.marks = 90
print("Modified values:", student.student_name, student.marks)

'''Write a Python class named Student with two attributes student_id, student_name. 
Add a new attribute student_class and display the entire attribute and the values of the class. 
Now remove the student_name attribute and display the entire attribute with values.'''
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

student = Student(1, "John")
print("Attributes before adding student_class:", student.__dict__)

student.student_class = "Math"
print("Attributes after adding student_class:", student.__dict__)

del student.student_name
print("Attributes after removing student_name:", student.__dict__)

'''Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. 
Create a function to display all attributes and their values in the Student class.'''
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None
    
    def display_attributes(self):
        attributes = self.__dict__
        for key, value in attributes.items():
            print(f"{key}: {value}")

student = Student(1, "Alice")
student.student_class = "Math"
student.display_attributes()

'''Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. 
Print all the attributes of the student1, student2 instances with their values in the given format.'''

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    
    def display_attributes(self):
        attributes = self.__dict__
        for key, value in attributes.items():
            print(f"{key}: {value}")

student1 = Student(1, "Alice")
student1.student_class = "Math"
student2 = Student(2, "Bob")
student2.student_class = "Science"

print("Student 1:")
student1.display_attributes()
print("\nStudent 2:")
student2.display_attributes()

'''Write a Python class to convert an integer to a Roman numeral.'''
class IntegerToRoman:
    def __init__(self):
        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def int_to_roman(self, num):
        roman_numeral = ''
        for value, symbol in self.value_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

converter = IntegerToRoman()
print(converter.int_to_roman(3549))

'''Write a Python class to convert a Roman numeral to an integer.'''
class RomanToInteger:
    def __init__(self):
        self.roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def roman_to_int(self, roman):
        total = 0
        prev_value = 0
        for symbol in reversed(roman):
            value = self.roman_map[symbol]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

converter = RomanToInteger()
print(converter.roman_to_int('MMMDXLIX'))

'''Write a Python class to check the validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
These brackets must be closed in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.'''
class ParenthesesValidator:
    def is_valid(self, s):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

validator = ParenthesesValidator()
print(validator.is_valid("()[]{}"))
print(validator.is_valid("({[)]"))

'''Write a Python class to get all possible unique subsets from a set of distinct integers.
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]'''
class Subsets:
    def get_subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [current + [num] for current in result]
        return result

subsets = Subsets()
print(subsets.get_subsets([4, 5, 6]))

'''Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
Note: There will be one solution for each input and do not use the same element twice.
Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4'''
class PairFinder:
    def find_pair(self, numbers, target):
        lookup = {}
        for i, num in enumerate(numbers):
            if target - num in lookup:
                return lookup[target - num], i
            lookup[num] = i

pair_finder = PairFinder()
print(pair_finder.find_pair([10, 20, 10, 40, 50, 60, 70], 50))

'''Write a Python class to find the three elements that sum to zero from a set of n real numbers.'''
class ThreeSumZero:
    def find_three_sum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result

three_sum = ThreeSumZero()
print(three_sum.find_three_sum([-25, -10, -7, -3, 2, 4, 8, 10]))

'''Write a Python class to implement pow(x, n).'''
class Power:
    def pow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result

power = Power()
print(power.pow(2, 10))
print(power.pow(2, -2))

'''Write a Python class to reverse a string word by word.'''
class ReverseWords:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

reverser = ReverseWords()
print(reverser.reverse_words('hello .py'))

'''Write a Python class that has two methods: get_String and print_String, get_String accept 
a string from the user and print_String prints the string in upper case.'''
class StringHandler:
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input("Enter a string: ")

    def print_String(self):
        print(self.s.upper())

handler = StringHandler()
handler.get_String()
handler.print_String()

'''Write a Python class named Rectangle constructed from length and width and a method that 
will compute the area of a rectangle.'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(10, 5)
print(rect.area())

'''Write a Python class named Circle constructed from a radius and two methods that will 
compute the area and the perimeter of a circle.'''
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")

'''Write a Python program to get the class name of an instance in Python.'''
class SampleClass:
    pass

instance = SampleClass()
print(f"The class name of the instance is: {instance.__class__.__name__}")

'''Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department 
and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.'''
class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            total_salary = self.emp_salary + overtime_amount
        else:
            total_salary = self.emp_salary
        return total_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")

employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

employee1.emp_assign_department("FINANCE")

employee1.print_employee_details()
print("Total Salary with 55 hours worked: ", employee1.calculate_emp_salary(55))

employee2.print_employee_details()
print("Total Salary with 45 hours worked: ", employee2.calculate_emp_salary(45))

employee3.print_employee_details()
employee4.print_employee_details()

'''Write a Python class Restaurant with attributes like menu_items, book_table, 
and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.'''
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = {}
        self.customer_orders = []

    def add_item_to_menu(self, item_name, item_price):
        self.menu_items[item_name] = item_price
        print(f"Added {item_name} to the menu with price {item_price}.")

    def book_table(self, customer_name, table_number):
        if table_number not in self.booked_tables:
            self.booked_tables[table_number] = customer_name
            print(f"Table {table_number} has been booked by {customer_name}.")
        else:
            print(f"Table {table_number} is already booked by {self.booked_tables[table_number]}.")

    def customer_order(self, customer_name, order_items):
        order = {"customer_name": customer_name, "order_items": order_items}
        self.customer_orders.append(order)
        print(f"Order placed by {customer_name} for items {order_items}.")

    def print_menu(self):
        print("Menu:")
        for item_name, item_price in self.menu_items.items():
            print(f"{item_name}: ${item_price}")

    def print_table_reservations(self):
        print("Table Reservations:")
        for table_number, customer_name in self.booked_tables.items():
            print(f"Table {table_number}: {customer_name}")

    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"{order['customer_name']} ordered {order['order_items']}")

# Create a Restaurant instance
restaurant = Restaurant()

# Add items to the menu
restaurant.add_item_to_menu("Burger", 8.99)
restaurant.add_item_to_menu("Pizza", 12.99)
restaurant.add_item_to_menu("Pasta", 10.99)

# Book tables
restaurant.book_table("Alice", 1)
restaurant.book_table("Bob", 2)
restaurant.book_table("Alice", 3)

# Take customer orders
restaurant.customer_order("Alice", ["Burger", "Pasta"])
restaurant.customer_order("Bob", ["Pizza"])

# Print the menu
restaurant.print_menu()

# Print table reservations
restaurant.print_table_reservations()

# Print customer orders
restaurant.print_customer_orders()

'''Write a Python class BankAccount with attributes like account_number, balance, date_of_opening 
and customer_name, and methods like deposit, withdraw, and check_balance.'''
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

account = BankAccount("123456789", 1000.0, "2024-01-01", "John Doe")

account.deposit(500.0)

account.withdraw(200.0)

account.check_balance()

'''Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, 
and methods like add_item, update_item, and check_item_details.
Use a dictionary to store the item details, where the key is the item_id and the value is 
a dictionary containing the item_name, stock_count, and price.'''
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        if item_id not in self.items:
            self.items[item_id] = {'item_name': item_name, 'stock_count': stock_count, 'price': price}
            print(f"Item with ID {item_id} added successfully.")
        else:
            print(f"Item with ID {item_id} already exists.")

    def update_item(self, item_id, stock_count, price):
        if item_id in self.items:
            self.items[item_id]['stock_count'] = stock_count
            self.items[item_id]['price'] = price
            print(f"Item with ID {item_id} updated successfully.")
        else:
            print(f"Item with ID {item_id} does not exist.")

    def check_item_details(self, item_id):
        if item_id in self.items:
            print(f"Item ID: {item_id}")
            print(f"Item Name: {self.items[item_id]['item_name']}")
            print(f"Stock Count: {self.items[item_id]['stock_count']}")
            print(f"Price: {self.items[item_id]['price']}")
        else:
            print(f"Item with ID {item_id} does not exist.")

inventory = Inventory()

inventory.add_item(1, 'Chair', 20, 50)
inventory.add_item(2, 'Table', 10, 100)

inventory.update_item(1, 15, 60)

inventory.check_item_details(1)
inventory.check_item_details(3)
