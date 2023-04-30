"""
1. Write a Python program to Extract Unique values dictionary values?
"""
my_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}

unique_values = set(val for sublist in my_dict.values() for val in sublist)

print(unique_values)

##--------------------------------------------------------------------------------------------------------------##

"""
2. Write a Python program to find the sum of all items in a dictionary?
"""
my_dict = {'a': 100, 'b': 200, 'c': 300}

total_sum = sum(my_dict.values())

print(total_sum)

##--------------------------------------------------------------------------------------------------------------##

"""
3. Write a Python program to Merging two Dictionaries?
"""
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)

print(dict1)

##--------------------------------------------------------------------------------------------------------------##

"""
4. Write a Python program to convert key-values list to flat dictionary?
"""
keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = {keys[i]: values[i] for i in range(len(keys))}

print(my_dict)

##--------------------------------------------------------------------------------------------------------------##

"""
5. Write a Python program to insertion at the beginning in OrderedDict?
"""
from collections import OrderedDict

# create an OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# insert a new item at the beginning of the OrderedDict
od['d'] = 4
od.move_to_end('d', last=False)

print(od)

##--------------------------------------------------------------------------------------------------------------##

"""
6. Write a Python program to check order of character in string using OrderedDict()?
"""
from collections import OrderedDict

# define the input string
input_str = 'python'

# create an OrderedDict from the input string
od = OrderedDict.fromkeys(input_str)

# check if the characters in the input string are in order
if ''.join(od.keys()) == input_str:
    print('The characters in the string are in order')
else:
    print('The characters in the string are not in order')

    ##--------------------------------------------------------------------------------------------------------------##

"""
7. Write a Python program to sort Python Dictionaries by Key or Value?
"""
# define a dictionary
d = {'b': 2, 'a': 1, 'c': 3}

# sort the dictionary by keys
sorted_dict_keys = dict(sorted(d.items(), key=lambda x: x[0]))

# sort the dictionary by values
sorted_dict_values = dict(sorted(d.items(), key=lambda x: x[1]))

print(sorted_dict_keys)
print(sorted_dict_values)

##--------------------------------------------------------------------------------------------------------------##

