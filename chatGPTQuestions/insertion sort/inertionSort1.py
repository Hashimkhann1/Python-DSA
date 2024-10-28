


def insertionSort(arr):
    
    # length of the list
    n = len(arr)
    
    # lopping the list
    for i in range(1 , n):
        
        # item at position i
        key = arr[i]
        
        # item just before i
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            
            # swiping the numbers
            arr[j + 1] = arr[j]
            
            # decrementing the j
            j -= 1
            
        # placing the key it right position
        arr[j + 1] = key
        
    return arr
        

sortingList = [5, 2, 9, 1, 6]
print(insertionSort(sortingList))