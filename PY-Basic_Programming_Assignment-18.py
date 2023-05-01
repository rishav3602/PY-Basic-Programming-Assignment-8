"""
Question 1
Create a function that takes a list of non-negative integers and strings and return a new list
without the strings.
Examples
filter_list([1, 2, &quot;a&quot;, &quot;b&quot;]) ➞ [1, 2]
filter_list([1, &quot;a&quot;, &quot;b&quot;, 0, 15]) ➞ [1, 0, 15]
filter_list([1, 2, &quot;aasf&quot;, &quot;1&quot;, &quot;123&quot;, 123]) ➞ [1, 2, 123]
"""
def filter_list(lst):
    return [num for num in lst if type(num) == int]

    ##----------------------------------------------------------------------------------------------------------------##

"""
Question 2
The &quot;Reverser&quot; takes a string as input and returns that string in reverse order, with the
opposite case.
Examples
reverse(&quot;Hello World&quot;) ➞ &quot;DLROw OLLEh&quot;
reverse(&quot;ReVeRsE&quot;) ➞ &quot;eSrEvEr&quot;
reverse(&quot;Radar&quot;) ➞ &quot;RADAr&quot;
"""
def reverse(string):
    return string[::-1].swapcase()

    ##----------------------------------------------------------------------------------------------------------------##

"""
Question 3
You can assign variables from lists like this:
lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]
print(first) ➞ outputs 1
print(middle) ➞ outputs [2, 3, 4, 5]
print(last) ➞ outputs 6
With Python 3, you can assign variables from lists in a much more succinct way. Create
variables first, middle and last from the given list using destructuring assignment
(check the Resources tab for some examples), where:
first ➞ 1
middle ➞ [2, 3, 4, 5]
last ➞ 6

Your task is to unpack the list writeyourcodehere into three variables, being first,
middle, and last, with middle being everything in between the first and last element. Then
print all three variables.
"""
lst = [1, 2, 3, 4, 5, 6]
first, *middle, last = lst
print(first)
print(middle)
print(last)

##----------------------------------------------------------------------------------------------------------------##

"""
Question 4
Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1
"""
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

    ##----------------------------------------------------------------------------------------------------------------##

"""
Question 5
Write a function that moves all elements of one type to the end of the list.
Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
move_to_end([&quot;a&quot;, &quot;a&quot;, &quot;a&quot;, &quot;b&quot;], &quot;a&quot;) ➞ [&quot;b&quot;, &quot;a&quot;, &quot;a&quot;, &quot;a&quot;]
"""
def move_to_end(lst, element):
    return [x for x in lst if x != element] + [x for x in lst if x == element]

    ##----------------------------------------------------------------------------------------------------------------##
