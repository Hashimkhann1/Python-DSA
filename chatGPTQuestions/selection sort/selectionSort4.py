


def selectionSort(arr):
    
    arrLength = len(arr)
    
    for i in range(arrLength):
        
        min_index = i
        
        for j in range(i + 1 , arrLength):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
        
    return arr




# unSortedList = [15, 22, 15, 7, 22, 10, 3, 7]
unSortedList = [45.99, 19.99, 89.99, 35.50, 99.99, 12.75]
print(selectionSort(unSortedList))


def insertionSort(arr):
    
    arrLength = len(arr)
    
    for i in range(1 , arrLength):
        
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            
            arr[j + 1] = arr[j]
            
            j -= 1
            
        arr[j + 1] = key
        
    return arr
        


print("-----------------------------")
print(insertionSort(unSortedList))