

# ---------------------------------------------
# My Code 
# ---------------------------------------------

def binary_search(arr, target):

    left , right = 0 , len(arr) - 1
   
    while left <= right:
       mid = (left + right) // 2
       
       if arr[mid] == target:
           return mid
       elif arr[mid] < target:
           left = mid + 1
       else:
           right = mid - 1
    return -1





# ---------------------------------------------
# Chat GPT Code
# ---------------------------------------------


# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
        
#         if arr[mid] == target:
#           return mid
#         elif arr[mid] < target:  # Target is in the right half
#             left = mid + 1
#         else:  # Target is in the left half
#             print(mid)
#             right = mid - 1
#             print(right)
        
#     return -1





arr = [10, 20, 30, 40, 50, 60, 70 , 80]
target = 10

print(binary_search(arr, target))  # Output: 4 (index of 50)
