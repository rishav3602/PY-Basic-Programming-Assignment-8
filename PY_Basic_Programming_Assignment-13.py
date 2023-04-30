"""
Question 1:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated
sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
import math

C = 50
H = 30

D = input("Enter comma separated values of D: ")
D_list = D.split(",")

result_list = []
for d in D_list:
    Q = round(math.sqrt((2 * C * int(d))/H))
    result_list.append(Q)

result = ",".join(map(str, result_list))
print(result)

##-------------------------------------------------------------------------------------------------------------------##

"""
Question 2:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
"""
X, Y = input("Enter values of X and Y separated by comma: ").split(",")
X = int(X)
Y = int(Y)

result = [[0 for j in range(Y)] for i in range(X)]

for i in range(X):
    for j in range(Y):
        result[i][j] = i*j

print(result)

##-------------------------------------------------------------------------------------------------------------------##

"""
Question 3:
Write a program that accepts a comma separated sequence of words as input and prints the
words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""
words = input("Enter comma separated words: ")
words_list = words.split(",")

words_list.sort()

result = ",".join(words_list)
print(result)

"""
Question 4:
Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""
sentence = input("Enter sentence: ")
words_list = sentence.split()

unique_words_set = set(words_list)
unique_words_list = list(unique_words_set)
unique_words_list.sort()

result = " ".join(unique_words_list)
print(result)

##-------------------------------------------------------------------------------------------------------------------##

"""
Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10

DIGITS 3
"""
sentence = input("Enter sentence: ")
letters = 0
digits = 0

for char in sentence:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

result = "LETTERS {}\n\nDIGITS {}".format(letters, digits)
print(result)

##-------------------------------------------------------------------------------------------------------------------##

"""
Question 6:
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed, each
separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""
import re

passwords = input("Enter comma separated passwords: ")
password_list = passwords.split(",")

valid_passwords = []

for password in password_list:
    if len(password) < 6 or len(password) > 12:
        continue
    if not re.search("[a-z]", password):
        continue
    if not re.search("[0-9]", password):
        continue
    if not re.search("[A-Z]", password):
        continue
    if not re.search("[$#@]", password):
        continue
    valid_passwords.append(password)

result = ",".join(valid_passwords)
print(result)

##-------------------------------------------------------------------------------------------------------------------##
