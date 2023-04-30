"""
1. Write a Python program to find words which are greater than given length k?
"""
def find_long_words(str, k):
    words = str.split()
    long_words = [word for word in words if len(word) > k]
    return long_words

# Example usage
my_str = "The quick brown fox jumps over the lazy dog"
k = 4
print("Words longer than", k, "characters:")
print(find_long_words(my_str, k))

##-----------------------------------------------------------------------------------------------------------------##

"""
2. Write a Python program for removing i-th character from a string?
"""
def remove_char(str, i):
    new_str = str[:i] + str[i+1:]
    return new_str

# Example usage
my_str = "Python"
i = 2
print("String with the", i+1, "th character removed:")
print(remove_char(my_str, i))

##-----------------------------------------------------------------------------------------------------------------##

"""
3. Write a Python program to split and join a string?
"""
def split_and_join(str):
    words = str.split()
    new_str = "-".join(words)
    return new_str

# Example usage
my_str = "The quick brown fox"
print("String after splitting and joining:")
print(split_and_join(my_str))

##-----------------------------------------------------------------------------------------------------------------##

"""
4. Write a Python to check if a given string is binary string or not?
"""
def is_binary_string(str):
    for char in str:
        if char != '0' and char != '1':
            return False
    return True

# Example usage
my_str = "1010011"
if is_binary_string(my_str):
    print(my_str, "is a binary string")
else:
    print(my_str, "is not a binary string")

    ##-----------------------------------------------------------------------------------------------------------------##

"""
5. Write a Python program to find uncommon words from two Strings?
"""
def find_uncommon_words(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    uncommon_words = set1.symmetric_difference(set2)
    return uncommon_words

# Example usage
str1 = "The quick brown fox"
str2 = "The lazy dog jumps over the brown fox"
print("Uncommon words between two strings:")
print(find_uncommon_words(str1, str2))

##-----------------------------------------------------------------------------------------------------------------##

"""
6. Write a Python to find all duplicate characters in string?
"""
def find_duplicate_chars(str):
    duplicates = []
    for char in str:
        if str.count(char) > 1 and char not in duplicates:
            duplicates.append(char)
    return duplicates

# Example usage
my_str = "Hello, World!"
print("Duplicate characters in the string:")
print(find_duplicate_chars(my_str))

##-----------------------------------------------------------------------------------------------------------------##

"""
7. Write a Python Program to check if a string contains any special character?
"""
import re

def contains_special_char(string):
    pattern = re.compile(r'\W')
    if pattern.search(string):
        return True
    else:
        return False

# Example usage
string1 = "Hello world!"
string2 = "Python123"    

print(contains_special_char(string1))  
print(contains_special_char(string2))

##-----------------------------------------------------------------------------------------------------------------##

