"""
Question 1
Create a function that takes a number as an argument and returns True or False depending
on whether the number is symmetrical or not. A number is symmetrical when it is the same as
its reverse.
Examples
is_symmetrical(7227) ➞ True
is_symmetrical(12567) ➞ False
is_symmetrical(44444444) ➞ True
is_symmetrical(9939) ➞ False
is_symmetrical(1112111) ➞ True
"""

def is_symmetrical(num):
    return str(num) == str(num)[::-1]


"""
Question 2
Given a string of numbers separated by a comma and space, return the product of the
numbers.
Examples
multiply_nums(&quot;2, 3&quot;) ➞ 6
multiply_nums(&quot;1, 2, 3, 4&quot;) ➞ 24
multiply_nums(&quot;54, 75, 453, 0&quot;) ➞ 0
multiply_nums(&quot;10, -2&quot;) ➞ -20
"""

from functools import reduce

def multiply_nums(nums):
    num_list = nums.split(", ")
    num_list = [int(x) for x in num_list]
    return reduce(lambda x, y: x*y, num_list)


"""
Question 3
Create a function that squares every digit of a number.
Examples
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414
Notes
The function receives an integer and must return an integer.
"""

def square_digits(num):
    result = ""
    while num != 0:
        digit = num % 10
        squared_digit = str(digit ** 2)
        result += squared_digit
        num //= 10
    return int(result[::-1])


"""
Question 4
Create a function that sorts a list and removes all duplicate items from it.
Examples
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
setify([4, 4, 4, 4]) ➞ [4]
setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]
"""

def setify(lst):
    return list(set(sorted(lst)))


"""
Question 5
Create a function that returns the mean of all digits.
Examples
mean(42) ➞ 3
mean(12345) ➞ 3
mean(666) ➞ 6
Notes
 The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in
512 is (5+1+2)/3(number of digits) = 8/3=2).
 The mean will always  be an integer.
"""

def mean(num):
    digits = [int(d) for d in str(num)] # Extract digits
    total = sum(digits) # Calculate sum of digits
    return total // len(digits) # Calculate and return mean
