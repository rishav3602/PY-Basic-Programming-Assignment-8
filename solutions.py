"""
1. Write a Python Program to Add Two Matrices?
"""
X = [[1,2,3],
     [4 ,5,6],
     [7 ,8,9]]

Y = [[9,8,7],
     [6,5,4],
     [3,2,1]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)

"""
2. Write a Python Program to Multiply Two Matrices?
"""
X = [[1,2,3],
     [4 ,5,6],
     [7 ,8,9]]

Y = [[9,8,7],
     [6,5,4],
     [3,2,1]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)

"""
3. Write a Python Program to Transpose a Matrix?
"""
X = [[1,2],
     [3,4],
     [5,6]]

result = [[0,0,0],
          [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)

"""
4. Write a Python Program to Sort Words in Alphabetic Order?
"""
string = "this is a test string to sort words in alphabetical order"

words = string.split()

words.sort()

print("The sorted words are:")
for word in words:
   print(word)

"""
5. Write a Python Program to Remove Punctuation From a String?
"""
import string

string_with_punctuation = "Hello, World! This is a test string."

string_without_punctuation = string_with_punctuation.translate(str.maketrans("", "", string.punctuation))

print("String without punctuation:", string_without_punctuation)

