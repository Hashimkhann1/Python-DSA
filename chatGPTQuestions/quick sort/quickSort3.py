

def quickSort(arr , low , high):
    
    if low < high:
        pidx = partition(arr , low , high)
        quickSort(arr , low , pidx - 1)
        quickSort(arr , pidx + 1 , high)
    
    return arr


def partition(arr , low , high):
    
    pivot = arr[high]
    j = low - 1
    
    for i in range(low , high):
        
        if arr[i] > arr[high]:
            j += 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    j += 1
    temp = arr[j]
    arr[j] = pivot
    arr[high] = temp
    
    return j
    




unSortedList = [1, 9, 3, 7, 4, 6, 8]
n = len(unSortedList)
print(quickSort(unSortedList , 0 , n - 1))



def selectionSort(arr):
    
    arrrLength = len(arr)
    
    for i in range(arrrLength):
        
        min_index = i
        
        for j in range(i + 1 , arrrLength):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
    
    return arr
    



unSortedList1 = [1, 9, 3, 7, 4, 6, 8]
print(selectionSort(unSortedList1))



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
    

unSortedList2 = [1, 9, 3, 7, 4, 6, 8]
print(insertionSort(unSortedList2))