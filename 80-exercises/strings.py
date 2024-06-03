'''Write a Python program to calculate the length of a string.'''
def calculate_length(string):
    return len(string)

input_string = input("Enter a string: ")
print("Length of the string:", calculate_length(input_string))

'''Write a Python program to count the number of characters (character frequency) in a string.'''
def count_characters(string):
    char_frequency = {}
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency

sample_string = 'google.com'
print("Sample String:", sample_string)
print("Character Frequency:", count_characters(sample_string))

'''Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
If the string length is less than 2, return the empty string instead.'''
def get_first_and_last_two(string):
    if len(string) < 2:
        return ''
    else:
        return string[:2] + string[-2:]

sample_strings = ['w3resource', 'w3', ' w']
for sample_string in sample_strings:
    print("Sample String:", sample_string)
    print("Result:", get_first_and_last_two(sample_string))


'''Write a Python program to get a string from a given string where all occurrences of 
its first char have been changed to '$', except the first char itself.'''
def replace_first_char(string):
    first_char = string[0]
    modified_string = first_char + string[1:].replace(first_char, '$')
    return modified_string

sample_string = input("Enter a string: ")
print("Result:", replace_first_char(sample_string))

'''Write a Python program to get a single string from two given strings, separated 
by a space and swap the first two characters of each string.'''
def swap_first_two_chars(string1, string2):
    new_string1 = string2[:2] + string1[2:]
    new_string2 = string1[:2] + string2[2:]
    return new_string1 + ' ' + new_string2

first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")
print("Result:", swap_first_two_chars(first_string, second_string))

'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
 If the given string already ends with 'ing', add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.'''
def modify_string(string):
    if len(string) < 3:
        return string
    elif string[-3:] == 'ing':
        return string + 'ly'
    else:
        return string + 'ing'

input_string = input("Enter a string: ")
print("Result:", modify_string(input_string))

'''Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. 
If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.'''
def replace_not_poor(string):
    not_index = string.find('not')
    poor_index = string.find('poor')

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        return string[:not_index] + 'good' + string[poor_index + 4:]
    else:
        return string

input_string = input("Enter a string: ")
print("Result:", replace_not_poor(input_string))

'''Write a Python function that takes a list of words and return the longest word and the length of the longest one.'''
def longest_word(words):
    if not words:
        return None, 0
    
    longest = ''
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest = word
            max_length = len(word)
    
    return longest, max_length

sample_words = ['apple', 'banana', 'kiwi', 'orange', 'pineapple']
longest, length = longest_word(sample_words)

'''Write a Python program to remove the nth index character from a nonempty string.'''
def remove_nth_character(string, n):
    if n < 0 or n >= len(string):
        return "Invalid index"
    else:
        return string[:n] + string[n+1:]

input_string = input("Enter a non-empty string: ")
index = int(input("Enter the index of the character to remove: "))
result = remove_nth_character(input_string, index)

'''
Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
'''
def exchange_first_last(string):
    if len(string) <= 1:
        return string
    else:
        return string[-1] + string[1:-1] + string[0]

input_string_task10 = input("Enter a string: ")
result = exchange_first_last(input_string_task10)
print("Result:", result)

'''
Write a Python program to remove characters that have odd index values in a given string.
'''
def remove_odd_index_chars(string):
    return string[::2]

input_string = input("Enter a string: ")
result = remove_odd_index_chars(input_string)
print("Result:", result)

'''
Write a Python program to count the occurrences of each word in a given sentence.
'''
def count_word_occurrences(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

input_sentence = input("Enter a sentence: ")
result = count_word_occurrences(input_sentence)
print("Result:", result)

'''
Write a Python script that takes input from the user and displays that input back in upper and lower cases.
'''
def display_upper_lower_case(string):
    upper_case = string.upper()
    lower_case = string.lower()
    return upper_case, lower_case

input_string = input("Enter a string: ")
upper_case_result, lower_case_result = display_upper_lower_case(input_string)
print("Upper Case Result:", upper_case_result)
print("Lower Case Result:", lower_case_result)

'''
Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
'''
def distinct_sorted_words(words):
    distinct_words = sorted(set(words))
    return distinct_words

input_words = input("Enter comma-separated words: ").split(', ')
result = distinct_sorted_words(input_words)
print("Result:", result)

'''
Write a Python function to create an HTML string with tags around the word(s).
'''
def add_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"

tag = input("Enter HTML tag: ")
word = input("Enter a word: ")
result = add_tags(tag, word)
print("Result:", result)

'''
Write a Python function to insert a string in the middle of a string.
'''
def insert_string_middle(main_string, insert_string):
    middle_index = len(main_string) // 2
    return main_string[:middle_index] + insert_string + main_string[middle_index:]

main_string = input("Enter the main string: ")
insert_string = input("Enter the string to insert: ")
result = insert_string_middle(main_string, insert_string)
print("Result:", result)

'''
Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
'''
def insert_end(string):
    return string[-2:] * 4

input_string = input("Enter a string: ")
result = insert_end(input_string)
print("Result:", result)

'''
Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
'''
def first_three(string):
    if len(string) < 3:
        return string
    else:
        return string[:3]

input_string = input("Enter a string: ")
result = first_three(input_string)
print("Result:", result)

'''
Write a Python program to get the last part of a string before a specified character.
'''
def get_last_part(string, delimiter):
    return string.rsplit(delimiter, 1)[0]

delimiter = input("Enter the delimiter: ")
string = input("Enter a string: ")
result = get_last_part(string, delimiter)
print("Result:", result)

'''
Write a Python function to reverse a string if its length is a multiple of 4.
'''
def reverse_string_if_multiple_of_4(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string

input_string = input("Enter a string: ")
result = reverse_string_if_multiple_of_4(input_string)
print("Result:", result)
