

# Binary Search Problem: Find the First Occurrence of Target

# Problem Statement:

# Given a sorted array of integers, write a function that uses binary search to find the first occurrence
# of a target value. If the target is found, return its index. If the target is not found, return -1.

# Input: arr = [1, 2, 4, 4, 4, 5, 6], target = 4
# Output: 2

# Input: arr = [2, 3, 5, 7, 9], target = 6
# Output: -1



def binary_search_first_occurrence(arr, target):
    
    left , right = 0 , len(arr) - 1
    result = -1
    
    while left <= right:
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
                
    return result



arr1 = [1, 2, 4, 4, 4, 5, 6]
target1 = 4

print(binary_search_first_occurrence(arr1 , target1))

arr2 = [2, 3, 5, 7, 9]
target2 = 6
print(binary_search_first_occurrence(arr2 , target2))