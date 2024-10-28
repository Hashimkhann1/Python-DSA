



def insertionSort(arr):
    n = len(arr)
    
    for i in range(1 , n):
        
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr


sortingList = [-100, -5, 0, 12, 33, 33, 33, 54, 54, 78, 100, 100]
print(insertionSort(sortingList))