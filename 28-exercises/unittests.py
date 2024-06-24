import os
import unittest

'''Write a Python unit test program to check if a given number is prime or not.'''
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True

'''Write a Python unit test program to check if a list is sorted in ascending order.'''
def is_sorted_ascending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

'''Write a Python unit test program that checks if two lists are equal.'''
def lists_equal(list1, list2):
    return list1 == list2

'''Write a Python unit test program to check if a string is a palindrome.'''
def is_palindrome(string):
    return string == string[::-1]

'''Write a Python unit test program to check if a file exists in a specified directory.'''
def file_exists(directory, filename):
    return os.path.isfile(os.path.join(directory, filename))

'''Write a Python unit test that checks if a function handles floating-point calculations accurately.'''
def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

'''Write a Python unit test program to check if a function handles multi-threading correctly.'''
import threading

def perform_task():
    result = 0
    for i in range(1, 100000):
        result += i
    return result

'''Write a Python unit test program to check if a database connection is successful.'''
import sqlite3

def database_connection():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

'''Write a Python unit test program to check if a database query returns the expected results.'''
class Connection:
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL)")
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES ('Ylva Guiomar', 1800.0)")
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES ('Scott Gregorius', 2100.0)")
        self.conn.commit()
        return self.cursor

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

'''Write a Python unit test program to check if a function correctly parses and validates input data.'''
def parse_and_validate_input(data):
    if isinstance(data, str) and data.isnumeric():
        return int(data) > 0
    return False

class TestPrograms(unittest.TestCase):
    '''Write a Python unit test program to check if a given number is prime or not.'''
    def test_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(1))

    '''Write a Python unit test program to check if a list is sorted in ascending order.'''
    def test_is_sorted_ascending(self):
        self.assertTrue(is_sorted_ascending([1, 2, 3, 4, 5]))
        self.assertFalse(is_sorted_ascending([7, 3, 8, 1]))

    '''Write a Python unit test program that checks if two lists are equal.'''
    def test_lists_equal(self):
        self.assertTrue(lists_equal([1, 2, 3], [1, 2, 3]))
        self.assertFalse(lists_equal([1, 2, 3], [3, 2, 1]))

    '''Write a Python unit test program to check if a string is a palindrome.'''
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("hello"))

    '''Write a Python unit test program to check if a file exists in a specified directory.'''
    def test_existing_file(self):
        directory = 'C:/Users/macie/OneDrive/Pulpit/repo/28-exercises/'
        filename = 'temp.txt'
        self.assertTrue(file_exists(directory, filename), "The file does not exist in the specified directory")

    def test_nonexistent_file(self):
        directory = '/path/txt'
        filename = 'test2.txt'
        self.assertFalse(file_exists(directory, filename), "The file exists in the specified directory")
        
    def test_nonexistent_file(self):
        directory = '/path/txt'
        filename = 'test2.txt'
        self.assertFalse(file_exists(directory, filename), "The file exists in the specified directory")

    '''Write a Python unit test that checks if a function handles floating-point calculations accurately.'''
    def test_addition(self):
        self.assertAlmostEqual(addition(0.3, 0.5), 0.8, places=6)

    def test_multiplication(self):
        self.assertAlmostEqual(multiplication(0.5, 0.3), 0.15, places=6)

    '''Write a Python unit test program to check if a function handles multi-threading correctly.'''
    def test_multi_threading(self):
        num_threads = 10
        threads = []

        for _ in range(num_threads):
            t = threading.Thread(target=perform_task)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        for t in threads:
            self.assertFalse(t.is_alive())

    '''Write a Python unit test program to check if a database connection is successful.'''
    def test_database_connection(self):
        self.assertEqual(database_connection(), (1,))


    '''Write a Python unit test program to check if a database query returns the expected results.'''
    def setUp(self):
        self.connection = Connection()
        self.cursor = self.connection.setUp()

    def tearDown(self):
        self.connection.tearDown()

    def test_database_query(self):
        self.cursor.execute("SELECT name, salary FROM employees ORDER BY name")
        results = self.cursor.fetchall()
        expected_results = [('Scott Gregorius', 2100.0), ('Ylva Guiomar', 1800.0)]
        self.assertEqual(results, expected_results)

    '''Write a Python unit test program to check if a function correctly parses and validates input data.'''
    def test_valid_input(self):
        data = "100"
        result = parse_and_validate_input(data)
        self.assertTrue(result)

    def test_invalid_input(self):
        data = "Hello"
        result = parse_and_validate_input(data)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()