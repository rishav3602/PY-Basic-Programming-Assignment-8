"""
1. Write a Python program to find sum of elements in list?
"""
def sum_of_list(list):
    sum = 0
    for element in list:
        sum += element
    return sum

# Example usage
my_list = [1, 2, 3, 4, 5]
print("Sum of elements in the list:", sum_of_list(my_list))


"""
2. Write a Python program to Multiply all numbers in the list?
"""
def multiply_list(list):
    result = 1
    for element in list:
        result *= element
    return result

# Example usage
my_list = [1, 2, 3, 4, 5]
print("Multiplication of all elements in the list:", multiply_list(my_list))

"""
3. Write a Python program to find smallest number in a list?
"""
def find_smallest(list):
    smallest = list[0]
    for element in list:
        if element < smallest:
            smallest = element
    return smallest

# Example usage
my_list = [5, 3, 7, 1, 8, 2]
print("Smallest element in the list:", find_smallest(my_list))

"""
4. Write a Python program to find largest number in a list?
"""
def find_largest(list):
    largest = list[0]
    for element in list:
        if element > largest:
            largest = element
    return largest

# Example usage
my_list = [5, 3, 7, 1, 8, 2]
print("Largest element in the list:", find_largest(my_list))

"""
5. Write a Python program to find second largest number in a list?
"""
def find_second_largest(list):
    largest = max(list)
    second_largest = list[0]
    for element in list:
        if element > second_largest and element < largest:
            second_largest = element
    return second_largest

# Example usage
my_list = [5, 3, 7, 1, 8, 2]
print("Second largest element in the list:", find_second_largest(my_list))

"""
6. Write a Python program to find N largest elements from a list?
"""
def find_n_largest(list, n):
    list.sort(reverse=True)
    return list[:n]

# Example usage
my_list = [5, 3, 7, 1, 8, 2]
n = 3
print("Top", n, "largest elements in the list:", find_n_largest(my_list, n))

"""
7. Write a Python program to print even numbers in a list?
"""
def print_even(list):
    for element in list:
        if element % 2 == 0:
            print(element)

# Example usage
my_list = [5, 3, 7, 1, 8, 2]
print("Even numbers in the list:")
print_even(my_list)

"""
8. Write a Python program to print odd numbers in a List?
"""
def print_odd(list):
    for element in list:
        if element % 2 != 0:
            print(element)

# Example usage
my_list = [5, 3, 7, 1, 8, 2]
print("Odd numbers in the list:")
print_odd(my_list)

"""
9. Write a Python program to Remove empty List from List?
"""
def remove_empty_lists(list):
    new_list = [element for element in list if element]
    return new_list

# Example usage
my_list = [[], [1, 2, 3], [], [], [4, 5], [], [6], []]
print("Original list:", my_list)
new_list = remove_empty_lists(my_list)
print("List after removing empty lists:", new_list)

"""
10. Write a Python program to Cloning or Copying a list?
"""
def clone_list(list):
    return list.copy()

# Example usage
my_list = [1, 2, 3, 4, 5]
new_list = clone_list(my_list)
print("Original list:", my_list)
print("Cloned list:", new_list)

"""
11. Write a Python program to Count occurrences of an element in a list?
"""
def count_occurrences(list, element):
    count = 0
    for item in list:
        if item == element:
            count += 1
    return count

# Example usage
my_list = [1, 2, 3, 2, 4, 2, 5]
element = 2
print("Number of occurrences of", element, "in the list:", count_occurrences(my_list, element))

##-----------------------------------------------------------------------------------------------------------------##
