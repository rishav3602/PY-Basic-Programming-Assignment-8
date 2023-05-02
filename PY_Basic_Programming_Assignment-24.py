"""
Question1
Create a function that takes an integer and returns a list from 1 to the given number, where:
1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the
number).
2. If the number cannot be divided evenly by 4, simply return the number.
Examples
amplify(4) ➞ [1, 2, 3, 40]
amplify(3) ➞ [1, 2, 3]
amplify(25) ➞ [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160,
17, 18, 19, 200, 21, 22, 23, 240, 25]
Notes
 The given integer will always be equal to or greater than 1.
 Include the number (see example above).
 To perform this problem with its intended purpose, try doing it with list
comprehensions. If that&#39;s too difficult, just solve the challenge any way you can.
"""

def amplify(n):
    result = []
    for i in range(1, n+1):
        if i % 4 == 0:
            result.append(i * 10)
        else:
            result.append(i)
    return result



"""
Question2
Create a function that takes a list of numbers and return the number that&#39;s unique.
Examples
unique([3, 3, 3, 7, 3, 3]) ➞ 7
unique([0, 0, 0.77, 0, 0]) ➞ 0.77
unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0
Notes
Test cases will always have exactly one unique number while all others are the same.
"""

def unique(lst):
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    for key, value in freq_dict.items():
        if value == 1:
            return key


"""
Question3
Your task is to create a Circle constructor that creates a circle with a radius provided by an
argument. The circles constructed must have two getters getArea() (PIr^2) and
getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).

For help with this class, I have provided you with a Rectangle constructor which you can use
as a base example.
Examples
circy = Circle(11)
circy.getArea()
# Should return 380.132711084365
circy = Circle(4.44)
circy.getPerimeter()
# Should return 27.897342763877365
Notes
Round results up to the nearest integer.
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.ceil(math.pi * self.radius ** 2)

    def getPerimeter(self):
        return math.ceil(2 * math.pi * self.radius)


"""
Question4
Create a function that takes a list of strings and return a list, sorted from shortest to longest.
Examples
sort_by_length([&quot;Google&quot;, &quot;Apple&quot;, &quot;Microsoft&quot;])
➞ [&quot;Apple&quot;, &quot;Google&quot;, &quot;Microsoft&quot;]
sort_by_length([&quot;Leonardo&quot;, &quot;Michelangelo&quot;, &quot;Raphael&quot;, &quot;Donatello&quot;])
➞ [&quot;Raphael&quot;, &quot;Leonardo&quot;, &quot;Donatello&quot;, &quot;Michelangelo&quot;]
sort_by_length([&quot;Turing&quot;, &quot;Einstein&quot;, &quot;Jung&quot;])
➞ [&quot;Jung&quot;, &quot;Turing&quot;, &quot;Einstein&quot;]
Notes
All test cases contain lists with strings of different lengths, so you won&#39;t have to deal with
multiple strings of the same length.
"""

def sort_by_length(lst):
    return sorted(lst, key=len)

# example usage
words = ["Google", "Apple", "Microsoft"]
sorted_words = sort_by_length(words)
print(sorted_words) # Output: ["Apple", "Google", "Microsoft"]


"""
Question5
Create a function that validates whether three given integers form a Pythagorean triplet. The
sum of the squares of the two smallest integers must equal the square of the largest number to
be validated.
"""

def is_pythagorean_triplet(a, b, c):
    # Find the squares of a, b, and c
    a_squared = a ** 2
    b_squared = b ** 2
    c_squared = c ** 2
    
    # Find the sum of the squares of the two smallest integers
    sum_of_squares = a_squared + b_squared if a_squared + b_squared < c_squared else b_squared + c_squared if b_squared + c_squared < a_squared else a_squared + c_squared
    
    # Check if the sum of squares is equal to the square of the largest integer
    if sum_of_squares == c_squared:
        return True
    else:
        return False
