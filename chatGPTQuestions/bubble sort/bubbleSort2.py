


def bubbleSort(arr):
    
    arrLength = len(arr)
    
    for i in range(arrLength):
        
        swapped = False
        
        for j in range(0 , arrLength - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
                swapped = True
                
        if not swapped:
            break
        
    return arr 



unSortedList = [1, 2, 3, 4, 5, 6]
print(bubbleSort(unSortedList))