
# 2. Negative Numbers:
# Sort the following list containing both positive and negative numbers using Selection Sort:



def selectionSort(arr):
    
    arrLength = len(arr)
    
    for i in range(arrLength):
        
        min_index = i
        
        for j in range(i + 1 , arrLength):
            
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
        
    return arr


unSortedList = [3, -1, -9, 8, 5, -4, 7]
print(selectionSort(unSortedList))