"""
Question 1:
Define a class with a generator which can iterate the numbers, which are divisible by
7, between a given range 0 and n.
"""
class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def divisible_by_seven(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

# Example usage:
gen = DivisibleBySeven(50).divisible_by_seven()
for num in gen:
    print(num)
    ##----------------------------------------------------------------------------------------------------------------##


"""
Question 2:
Write a program to compute the frequency of the words from the input. The output
should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""
text = input().split()

word_freq = {}
for word in text:
    word_freq[word] = word_freq.get(word, 0) + 1

words = list(word_freq.keys())
words.sort()

for word in words:
    print( % (word, word_freq[word]))
    ##----------------------------------------------------------------------------------------------------------------##


"""
Question 3:

Define a class Person and its two child classes: Male and Female. All classes have a
method &quot;getGender&quot; which can print &quot;Male&quot; for Male class and &quot;Female&quot; for Female
class.
"""
class Person:
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"
        ##----------------------------------------------------------------------------------------------------------------##


"""
Question 4:
Please write a program to generate all sentences where subject is in [&quot;I&quot;, &quot;You&quot;] and
verb is in [&quot;Play&quot;, &quot;Love&quot;] and the object is in [&quot;Hockey&quot;,&quot;Football&quot;].
"""
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            print(subject + " " + verb + " " + obj)
            ##----------------------------------------------------------------------------------------------------------------##


"""
Question 5:
Please write a program to compress and decompress the string &quot;hello world!hello
world!hello world!hello world!&quot;.
"""
import gzip

text = b"hello world!hello world!hello world!hello world!"

# Compress the text
compressed = gzip.compress(text)

# Decompress the text
decompressed = gzip.decompress(compressed)

print(decompressed)
##----------------------------------------------------------------------------------------------------------------##


"""
Question 6:
Please write a binary search function which searches an item in a sorted list. The
function should return the index of element to be searched in the list.
"""
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1
    ##----------------------------------------------------------------------------------------------------------------##

