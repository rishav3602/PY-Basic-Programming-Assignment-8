
"""
1. Write a Python program to check if the given number is a Disarium Number?
"""

def is_disarium(num):
    n = str(num)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])**(i+1)
    if sum == num:
        return True
    else:
        return False

# Example usage
num = 175
if is_disarium(num):
    print(num, "is a Disarium Number")
else:
    print(num, "is not a Disarium Number")

##------------------------------------------------------------------------------------------------------------------##


"""
2. Write a Python program to print all disarium numbers between 1 to 100?
"""

def disarium_numbers():
    for i in range(1, 101):
        if is_disarium(i):
            print(i)

# Example usage
disarium_numbers()
##------------------------------------------------------------------------------------------------------------------##

"""
3. Write a Python program to check if the given number is Happy Number?
"""
def is_happy(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit**2
        num //= 10
    if sum == 1:
        return True
    elif sum == 4:  # 4 is an unhappy number
        return False
    else:
        return is_happy(sum)

# Example usage
num = 19
if is_happy(num):
    print(num, "is a Happy Number")
else:
    print(num, "is not a Happy Number")

##------------------------------------------------------------------------------------------------------------------##

"""
4. Write a Python program to print all happy numbers between 1 and 100?
"""

def happy_numbers():
    for i in range(1, 101):
        if is_happy(i):
            print(i)

# Example usage
happy_numbers()
##------------------------------------------------------------------------------------------------------------------##

"""
5. Write a Python program to determine whether the given number is a Harshad Number?
"""

def is_harshad(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    if num % sum == 0:
        return True
    else:
        return False

# Example usage
num = 18
if is_harshad(num):
    print(num, "is a Harshad Number")
else:
    print(num, "is not a Harshad Number")

##------------------------------------------------------------------------------------------------------------------##


"""
6. Write a Python program to print all pronic numbers between 1 and 100?
"""
def pronic_numbers():
    for i in range(1, 10):
        for j in range(1, 10):
            if i != j:
                num = i * (i+1)
                if num >= 1 and num <= 100:
                    print(num)

# Example usage
pronic_numbers()
##------------------------------------------------------------------------------------------------------------------##

