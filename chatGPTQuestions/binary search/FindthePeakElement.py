

# Binary Search Problem: Find the Peak Element

# Problem Statement:

# A peak element in an array is an element that is strictly greater than its neighbors. 
# Given an array arr, find any peak element and return its index. The array may contain
# multiple peaks, and you can return the index of any one of them.

# Note: In the case of an edge element, we consider only one neighbor for comparison.
# You must implement this problem using a binary search approach.




# Input: arr = [1, 2, 3, 1]
# Output: 2
# Explanation: The element at index 2 (which is 3) is a peak because it is greater than its neighbors (2 and 1).

# Input: arr = [1, 2, 1, 3, 5, 6, 4]
# Output: 5
# Explanation: The element at index 5 (which is 6) is a peak because it is greater than its neighbors (5 and 4).



def find_peak_element(arr):
    left , right = 0 , len(arr) - 1
    
    while left < right:
        
        mid = (left + right) // 2
        
        if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
            return mid
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
        
        
        
    


arr1 = [1, 2, 3, 1]
print(find_peak_element(arr1))

arr2 = [1, 2, 1, 3, 5, 6, 4]
print(find_peak_element(arr2))