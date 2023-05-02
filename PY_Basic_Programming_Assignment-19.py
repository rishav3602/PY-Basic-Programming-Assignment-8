"""
Question1
Create a function that takes a string and returns a string in which each character is repeated
once.
Examples
double_char(&quot;String&quot;) ➞ &quot;SSttrriinngg&quot;
double_char(&quot;Hello World!&quot;) ➞ &quot;HHeelllloo WWoorrlldd!!&quot;
double_char(&quot;1234!_ &quot;) ➞ &quot;11223344!!__ &quot;
"""
def double_char(string):
    return ''.join([char*2 for char in string])

##-------------------------------------------------------------------------------------------------------------------##S

"""
Question2
Create a function that reverses a boolean value and returns the string &quot;boolean expected&quot;
if another variable type is given.
Examples
reverse(True) ➞ False
reverse(False) ➞ True
reverse(0) ➞ &quot;boolean expected&quot;
reverse(None) ➞ &quot;boolean expected&quot;
"""
def reverse(arg):
    if type(arg) != bool:
        return 'boolean expected'
    return not arg

##-------------------------------------------------------------------------------------------------------------------##S

"""
Question3
Create a function that returns the thickness (in meters) of a piece of paper after folding it n
number of times. The paper starts off with a thickness of 0.5mm.
Examples
num_layers(1) ➞ &quot;0.001m&quot;
# Paper folded once is 1mm (equal to 0.001m)
num_layers(4) ➞ &quot;0.008m&quot;
# Paper folded 4 times is 8mm (equal to 0.008m)
num_layers(21) ➞ &quot;1048.576m&quot;
# Paper folded 21 times is 1048576mm (equal to 1048.576m)
"""
def num_layers(n):
    thickness_mm = 0.5 * 2**n
    thickness_m = thickness_mm / 1000
    return '{:.3f}m'.format(thickness_m)

##-------------------------------------------------------------------------------------------------------------------##S

"""
Question4

Create a function that takes a single string as argument and returns an ordered list containing
the indices of all capital letters in the string.
Examples
index_of_caps(&quot;eDaBiT&quot;) ➞ [1, 3, 5]
index_of_caps(&quot;eQuINoX&quot;) ➞ [1, 3, 4, 6]
index_of_caps(&quot;determine&quot;) ➞ []
index_of_caps(&quot;STRIKE&quot;) ➞ [0, 1, 2, 3, 4, 5]
index_of_caps(&quot;sUn&quot;) ➞ [1]
"""
def index_of_caps(string):
    return [i for i, char in enumerate(string) if char.isupper()]

##-------------------------------------------------------------------------------------------------------------------##S

"""
Question5
Using list comprehensions, create a function that finds all even numbers from 1 to the given
number.
Examples
find_even_nums(8) ➞ [2, 4, 6, 8]
find_even_nums(4) ➞ [2, 4]
find_even_nums(2) ➞ [2]
"""
def find_even_nums(n):
    return [i for i in range(1, n+1) if i % 2 == 0]

##-------------------------------------------------------------------------------------------------------------------##S
