

def quickSort(arr , low , high):
    
    if low < high:
    
        pidx = partition(arr , low , high)
        quickSort(arr , low , pidx - 1)
        quickSort(arr , pidx + 1 , high)
    
    
    return arr


def partition(arr , low , high):
    
    pivot = arr[high]
    i = low - 1
   
    for j in range(low , high):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            
    i += 1
    temp = arr[i]
    arr[i] = pivot
    arr[high] = temp
    
    return i



unSortedList = [12, 4, 5, 3, 8, 7]
n = len(unSortedList)
print(quickSort(unSortedList , 0 , n - 1))


def selectionSort(arr):
    
    arrLength = len(arr)
    
    for i in range(arrLength):
        
        min_Index = i
        
        for j in range(i + 1 , arrLength):
            if arr[j] < arr[min_Index]:
                min_Index = j
        
        arr[i] , arr[min_Index] = arr[min_Index] , arr[i]
    
    return arr



unSortedList1 = [12, 4, 5, 3, 8, 7]
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
        


unSortedList2 = [12, 4, 5, 3, 8, 7]
print(insertionSort(unSortedList2))



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
    



unSortedList3 = [12, 4, 5, 3, 8, 7]
print(bubbleSort(unSortedList3))
