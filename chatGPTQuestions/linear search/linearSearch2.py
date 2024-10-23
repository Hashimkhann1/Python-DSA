


# Linear Search Problem: First Occurrence of the Target

# Problem Statement:

# Write a function that takes a 2D array (a list of lists) of integers and a target integer. 
# It should return the row and column index of the first occurrence of the target in the 2D array. 
# If the target is not found, return -1, -1.


# Input: 
# arr = [
#   [10, 25, 30],
#   [45, 50, 60],
#   [70, 80, 90]
# ]
# target = 50
# Output: 1, 1

# Input: 
# arr = [
#   [5, 8, 12],
#   [20, 25, 30]
# ]
# target = 100
# Output: -1, -1


# ------------------------------
# My Solution 
# ------------------------------

def linear_search_2d(arr , target):
    
    for i in range(len(arr)):
        if target not in arr[i]:
            continue
        else:
            for targt in range(len(arr[i])):
                if target == arr[i][targt]:
                    return [i , targt]
    
    return [-1 , -1]





arr1 = [
  [10, 25, 30],
  [45, 50, 60],
  [70, 80, 90]
]

target1 = 50

print(linear_search_2d(arr1 , target1))


arr2 = [
  [5, 8, 12],
  [20, 25, 30]
]

target2 = 100

print(linear_search_2d(arr2 , target2))




# ------------------------------
# Chat GPT Solution Solution 
# chat gpt just make some changes in code description is below.

# Key Changes Made:
# Removed the if target not in arr[i]: check, simplifying the logic.
# Combined both loops into one, reducing complexity and improving readability.

# ------------------------------


def linear_search_2d(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return [i, j]  # Return the row and column index directly
    return [-1, -1]  # Return if target is not found

arr1 = [
    [10, 25, 30],
    [45, 50, 60],
    [70, 80, 90]
]
target1 = 50

print(linear_search_2d(arr1, target1))  # Output: [1, 1]

arr2 = [
    [5, 8, 12],
    [20, 25, 30]
]
target2 = 100

print(linear_search_2d(arr2, target2))  # Output: [-1, -1]
