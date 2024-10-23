

# Problem Statement:

# Write a function that takes an array of integers and a target integer. 
# It should return the index of the target if it exists in the array. 
# If the target is not found, return -1

# Input: arr = [10, 25, 30, 45, 50], target = 30
# Output: 2

# Input: arr = [5, 8, 12, 20], target = 15
# Output: -1


def linear_search(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1






arr1 = [10, 25, 30, 45, 50]
target1 = 30
# Output: 2

arr2 = [5, 8, 12, 20]
target2 = 15
# Output: -1

print(linear_search(arr1 , target1))

print(linear_search(arr2 , target2))

