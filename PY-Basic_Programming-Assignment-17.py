"""
Question1. Create a function that takes three arguments a, b, c and returns the sum of the
numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.
evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
"""
def evenly_divisible(a, b, c):
    return sum(i for i in range(a, b+1) if i % c == 0)

##-------------------------------------------------------------------------------------------------------------------##
"""
Question2. Create a function that returns True if a given inequality expression is correct and
False otherwise.
Examples
correct_signs(&quot;3 &lt; 7 &lt; 11&quot;) ➞ True
correct_signs(&quot;13 &gt; 44 &gt; 33 &gt; 1&quot;) ➞ False
correct_signs(&quot;1 &lt; 2 &lt; 6 &lt; 9 &gt; 3&quot;) ➞ True
"""
def correct_signs(expr):
    return eval(expr)

##-------------------------------------------------------------------------------------------------------------------##
"""
Question3. Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels(&quot;the aardvark&quot;, &quot;#&quot;) ➞ &quot;th# ##rdv#rk&quot;
replace_vowels(&quot;minnie mouse&quot;, &quot;?&quot;) ➞ &quot;m?nn?? m??s?&quot;
replace_vowels(&quot;shakespeare&quot;, &quot;*&quot;) ➞ &quot;sh*k*sp**r*&quot;
"""
def replace_vowels(s, c):
    vowels = 'aeiouAEIOU'
    return ''.join([c if i in vowels else i for i in s])

##-------------------------------------------------------------------------------------------------------------------##
"""
Question4. Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

##-------------------------------------------------------------------------------------------------------------------##
"""
Question 5
Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: &quot;abcbba&quot;
String2: &quot;abcbda&quot;
Hamming Distance: 1 - &quot;b&quot; vs. &quot;d&quot; is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance(&quot;abcde&quot;, &quot;bcdef&quot;) ➞ 5
hamming_distance(&quot;abcde&quot;, &quot;abcde&quot;) ➞ 0
hamming_distance(&quot;strong&quot;, &quot;strung&quot;) ➞ 1
"""
def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

##-------------------------------------------------------------------------------------------------------------------##