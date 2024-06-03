'''Write a Python script to sort (ascending and descending) a dictionary by value.'''
def sort_dictionary_by_value(dictionary):
    ascending_sorted = dict(sorted(dictionary.items(), key=lambda x: x[1]))
    descending_sorted = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
    return ascending_sorted, descending_sorted

sample_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}
ascending_result, descending_result = sort_dictionary_by_value(sample_dict)
print("Ascending Result:", ascending_result)
print("Descending Result:", descending_result)

'''Write a Python script to add a key to a dictionary.'''
def add_key_to_dictionary(dictionary, key, value):
    dictionary[key] = value
    return dictionary

sample_dict = {0: 10, 1: 20}
key_to_add = 2
value_to_add = 30
result = add_key_to_dictionary(sample_dict, key_to_add, value_to_add)
print("Result:", result)

'''Write a Python script to concatenate the following dictionaries to create a new one.'''
def concatenate_dictionaries(dict1, dict2, dict3):
    return {**dict1, **dict2, **dict3}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = concatenate_dictionaries(dic1, dic2, dic3)
print("Result:", result)

'''Write a Python script to check whether a given key already exists in a dictionary.'''
def key_exists_in_dictionary(dictionary, key):
    return key in dictionary

sample_dict = {1: 'apple', 2: 'banana', 3: 'orange'}
key_to_check = 2
result = key_exists_in_dictionary(sample_dict, key_to_check)
print("Result:", result)

'''Write a Python program to iterate over dictionaries using for loops.'''
sample_dict = {'a': 1, 'b': 2, 'c': 3}

print("Iterating over keys:")
for key in sample_dict:
    print(key)

print("\nIterating over values:")
for value in sample_dict.values():
    print(value)

print("\nIterating over items:")
for key, value in sample_dict.items():
    print(key, value)

'''Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).'''
def generate_square_dictionary(n):
    return {num: num ** 2 for num in range(1, n + 1)}

n = 5
result = generate_square_dictionary(n)
print("Result:", result)

'''Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.'''
square_dict = {num: num ** 2 for num in range(1, 16)}
print("Result:", square_dict)

'''Write a Python script to merge two Python dictionaries.'''
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result = merge_dictionaries(dict1, dict2)
print("Result:", result)

'''Write a Python program to iterate over dictionaries using for loops.'''
sample_dict = {'a': 1, 'b': 2, 'c': 3}

print("Iterating over keys:")
for key in sample_dict:
    print(key)

print("\nIterating over values:")
for value in sample_dict.values():
    print(value)

print("\nIterating over items:")
for key, value in sample_dict.items():
    print(key, value)

'''Write a Python program to sum all the items in a dictionary.'''
def sum_dictionary_values(dictionary):
    return sum(dictionary.values())

sample_dict = {'a': 10, 'b': 20, 'c': 30}
result = sum_dictionary_values(sample_dict)
print("Result:", result)

'''Write a Python program to multiply all the items in a dictionary.'''
def multiply_dictionary_values(dictionary):
    result = 1
    for value in dictionary.values():
        result *= value
    return result

sample_dict = {'a': 2, 'b': 3, 'c': 4}
result = multiply_dictionary_values(sample_dict)
print("Result:", result)

'''Write a Python program to remove a key from a dictionary.'''
def remove_key_from_dictionary(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

sample_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'
result = remove_key_from_dictionary(sample_dict, key_to_remove)
print("Result:", result)

'''Write a Python program to map two lists into a dictionary.'''
def map_lists_to_dictionary(keys, values):
    return dict(zip(keys, values))

keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = map_lists_to_dictionary(keys, values)
print("Result:", result)

'''Write a Python program to sort a given dictionary by key.'''
def sort_dictionary_by_key(dictionary):
    return dict(sorted(dictionary.items()))

sample_dict = {'b': 3, 'a': 1, 'c': 2}
result = sort_dictionary_by_key(sample_dict)
print("Result:", result)

'''Write a Python program to get the maximum and minimum values of a dictionary.'''
def get_max_min_dictionary_values(dictionary):
    if len(dictionary) == 0:
        return None, None
    return max(dictionary.values()), min(dictionary.values())

sample_dict = {'a': 10, 'b': 20, 'c': 5}
max_value, min_value = get_max_min_dictionary_values(sample_dict)
print("Max Value:", max_value)
print("Min Value:", min_value)

'''Write a Python program to get a dictionary from an object's fields.'''
class Object:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

obj = Object()
result = vars(obj)
print("Result:", result)

'''Write a Python program to remove duplicates from the dictionary.'''
def remove_duplicates_from_dictionary(dictionary):
    return dict(set(dictionary.items()))

sample_dict = {'a': 1, 'b': 2, 'c': 1}
result = remove_duplicates_from_dictionary(sample_dict)
print("Result:", result)

'''Write a Python program to check if a dictionary is empty or not.'''
def is_dictionary_empty(dictionary):
    return len(dictionary) == 0

sample_dict = {}
result = is_dictionary_empty(sample_dict)
print("Result:", result)

'''Write a Python program to combine two dictionary by adding values for common keys.'''
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
result = Counter(d1) + Counter(d2)
print("Result:", result)

'''Write a Python program to print all distinct values in a dictionary.'''
L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

u_value = set(val for dic in L for val in dic.values())

print("Unique Values: ", u_value) 
