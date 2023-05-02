"""
Question1
Create a function that takes three parameters where:
 x is the start of the range (inclusive).
 y is the end of the range (inclusive).
 n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third parameter n.
Return an empty list if there are no numbers that are divisible by n.
Examples
list_operation(1, 10, 3) ➞ [3, 6, 9]
list_operation(7, 9, 2) ➞ [8]
list_operation(15, 20, 7) ➞ []
"""
def list_operation(x, y, n):
    result = []
    for i in range(x, y+1):
        if i % n == 0:
            result.append(i)
    return result

"""
Question2
Create a function that takes in two lists and returns True if the second list follows the first list
by one element, and False otherwise. In other words, determine if the second list is the first
list shifted to the right by 1.
Examples
simon_says([1, 2], [5, 1]) ➞ True
simon_says([1, 2], [5, 5]) ➞ False
simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False
Notes
 Both input lists will be of the same length, and will have a minimum length of 2.
 The values of the 0-indexed element in the second list and the n-1th indexed element
in the first list do not matter.
"""
def simon_says(lst1, lst2):
    for i in range(len(lst1)-1):
        if lst1[i+1] != lst2[i]:
            return False
    return True

"""
Question3
A group of friends have decided to start a secret society. The name will be the first letter of
each of their names, sorted in alphabetical order.
Create a function that takes in a list of names and returns the name of the secret society.

Examples
society_name([&quot;Adam&quot;, &quot;Sarah&quot;, &quot;Malcolm&quot;]) ➞ &quot;AMS&quot;
society_name([&quot;Harry&quot;, &quot;Newt&quot;, &quot;Luna&quot;, &quot;Cho&quot;]) ➞ &quot;CHLN&quot;
society_name([&quot;Phoebe&quot;, &quot;Chandler&quot;, &quot;Rachel&quot;, &quot;Ross&quot;, &quot;Monica&quot;, &quot;Joey&quot;])
"""
def society_name(names):
    letters = [name[0] for name in names]
    return ''.join(sorted(letters))

"""
Question4
An isogram is a word that has no duplicate letters. Create a function that takes a string and
returns either True or False depending on whether or not it&#39;s an &quot;isogram&quot;.
Examples
is_isogram(&quot;Algorism&quot;) ➞ True
is_isogram(&quot;PasSword&quot;) ➞ False
# Not case sensitive.
is_isogram(&quot;Consecutive&quot;) ➞ False
Notes
 Ignore letter case (should not be case sensitive).
 All test cases contain valid one word strings.
"""
def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))

"""
Question5
Create a function that takes a string and returns True or False, depending on whether the
characters are in order or not.
Examples
is_in_order(&quot;abc&quot;) ➞ True
is_in_order(&quot;edabit&quot;) ➞ False
is_in_order(&quot;123&quot;) ➞ True
is_in_order(&quot;xyzz&quot;) ➞ True
Notes
You don&#39;t have to handle empty strings.
"""
def is_in_order(txt):

    # Convert the string to a list of characters
    chars = list(txt)
    # Sort the characters in ascending order
    sorted_chars = sorted(chars)
    # Check if the sorted characters are equal to the original characters
    return chars == sorted_chars
