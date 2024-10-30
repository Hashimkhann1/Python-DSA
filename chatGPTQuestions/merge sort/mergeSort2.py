

def mergeSort(arr):
    
    arrLength = len(arr)
    
    if arrLength <= 1:
        return arr
    
    mid = arrLength // 2
    l_half = arr[:mid]
    r_half = arr[mid:]
    l_half = mergeSort(l_half)
    r_half = mergeSort(r_half)
    return partition(l_half , r_half)

def partition(left , right):
    
    new = []
    i , j = 0 , 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
        
    new.extend(left[i:])
    new.extend(right[j:])
    
    return new
            

unSortedList = [6,3,9,5,2,8]
print(mergeSort(unSortedList))



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



unSortedList1 = [6,3,9,5,2,8]
print(insertionSort(unSortedList1))