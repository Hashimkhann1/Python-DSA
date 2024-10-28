


def selectionSort(arr):
    arrLength = len(arr)
    
    for i in range(arrLength):
        
        min_index = i
        
        for j in range(i + 1 , arrLength):
            if arr[j] < arr[min_index]:
                min_index = j
                print(min_index)
        
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
    
    return arr
    
    



unSortedList = [29, 10, 14, 37, 13]
print(selectionSort(unSortedList))

    