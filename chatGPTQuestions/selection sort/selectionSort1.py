


def selectionSort(arr):
    
    # length of the aaray
    n = len(arr)
    
    for i in range(n):
        
        # min index
        min_index = i
        
        for j in range(i + 1 , n):
            if arr[j] < arr[min_index]:
                min_index = j
                # print(min_index)
            
        arr[i] , arr[min_index] = arr[min_index] , arr[i]            
    return arr
         



unSortedList = [24,41,33,42,17]
print(selectionSort(unSortedList))