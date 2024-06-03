'''Write a Python program to sum all the items in a list.'''
def sum_list(items):
    return sum(items)

sample_list = [1, 2, 3, 4, 5]
result = sum_list(sample_list)
print("Result:", result)

'''Write a Python program to multiply all the items in a list.'''
def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result

sample_list = [1, 2, 3, 4, 5]
result = multiply_list(sample_list)
print("Result:", result)

'''Write a Python program to get the largest number from a list.'''
def get_largest_number(items):
    return max(items)

sample_list = [10, 20, 30, 40, 50]
result = get_largest_number(sample_list)
print("Result:", result)

'''Write a Python program to get the smallest number from a list.'''
def get_smallest_number(items):
    return min(items)

sample_list = [10, 20, 30, 40, 50]
result = get_smallest_number(sample_list)
print("Result:", result)

'''Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.'''
def count_matching_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

sample_list = ['abc', 'xyz', 'aba', '1221']
result = count_matching_strings(sample_list)
print("Result:", result)

'''Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.'''
def sort_list_last_element(tuples):
    return sorted(tuples, key=lambda x: x[-1])

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = sort_list_last_element(sample_list)
print("Result:", result)

'''Write a Python program to remove duplicates from a list.'''
def remove_duplicates(items):
    return list(set(items))

sample_list = [1, 2, 3, 1, 2, 3, 4, 5]
result = remove_duplicates(sample_list)
print("Result:", result)

'''Write a Python program to check if a list is empty or not.'''
def is_list_empty(items):
    return not bool(items)

sample_list = []
result = is_list_empty(sample_list)
print("Result:", result)

'''Write a Python program to clone or copy a list.'''
def clone_list(items):
    return items.copy()

sample_list = [1, 2, 3, 4, 5]
result = clone_list(sample_list)
print("Result:", result)

'''Write a Python program to find the list of words that are longer than n from a given list of words.'''
def words_longer_than_n(words, n):
    return [word for word in words if len(word) > n]

sample_list = ['apple', 'banana', 'orange', 'kiwi', 'grape']
n = 5
result = words_longer_than_n(sample_list, n)
print("Result:", result)

'''Write a Python function that takes two lists and returns True if they have at least one common member.'''
def have_common_member(list1, list2):
    return bool(set(list1) & set(list2))

sample_list1 = [1, 2, 3, 4, 5]
sample_list2 = [5, 6, 7, 8, 9]
result = have_common_member(sample_list1, sample_list2)
print("Result:", result)

'''Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.'''
def remove_elements_at_indices(lst, indices):
    return [elem for index, elem in enumerate(lst) if index not in indices]

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
indices_to_remove = [0, 4, 5]
result = remove_elements_at_indices(sample_list, indices_to_remove)
print("Result:", result)

'''Write a Python program to generate a 3*4*6 3D array whose each element is *.'''
def generate_3d_array(dim1, dim2, dim3):
    return [[['*' for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

result = generate_3d_array(3, 4, 6)
print("Result:", result)

'''Write a Python program to print the numbers of a specified list after removing even numbers from it.'''
def remove_even_numbers(lst):
    return [num for num in lst if num % 2 != 0]

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = remove_even_numbers(sample_list)
print("Result:", result)

'''Write a Python program to shuffle and print a specified list.'''
from random import shuffle

def shuffle_list(lst):
    shuffle(lst)
    return lst

sample_list = [1, 2, 3, 4, 5]
result = shuffle_list(sample_list)
print("Result:", result)

'''Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).'''
def generate_square_numbers():
    return [num ** 2 for num in range(1, 31)]

def get_first_and_last_5(lst):
    return lst[:5] + lst[-5:]

numbers = generate_square_numbers()
result = get_first_and_last_5(numbers)
print("Result:", result)

'''Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def are_all_prime(lst):
    return all(is_prime(num) for num in lst)

sample_list = [0, 3, 4, 7, 9]
result = are_all_prime(sample_list)
print("Result:", result)

'''Write a Python program to generate all permutations of a list in Python.'''
from itertools import permutations

def generate_permutations(lst):
    return list(permutations(lst))

sample_list = [1, 2, 3]
result = generate_permutations(sample_list)
print("Result:", result)

'''Write a Python program to calculate the difference between the two lists.'''
def calculate_difference(list1, list2):
    return list(set(list1) - set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = calculate_difference(list1, list2)
print("Result:", result)

'''Write a Python program to access the index of a list.'''
def access_index(lst, item):
    return [index for index, value in enumerate(lst) if value == item]

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item_to_find = 5
result = access_index(sample_list, item_to_find)
print("Result:", result)
