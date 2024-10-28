

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
        if arr[j] < arr[high]:
            i += 1
            arr[i] , arr[j] = arr[j] , arr[i]
        
    i += 1
    arr[i] , arr[high] = arr[high] , arr[i]
    
    return i




unSortedList = [5, 7, 9, 2, 1, 8, 4, 6, 3]
n = len(unSortedList)
print(quickSort(unSortedList , 0 , n - 1))



def selectionSort(arr):
    
    listLength = len(arr)
    
    for i in range(listLength):
        
        min_index = i
        
        for j in range(i + 1 , listLength):
            if arr[j] < arr[min_index]:
                
                min_index = j
                
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
    return arr



unSortedList1 = [5, 7, 9, 2, 1, 8, 4, 6, 3]
print('-------------------------')
print("Selection Sort")
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




unSortedList2 = [5, 7, 9, 2, 1, 8, 4, 6, 3]
print('--------------------------')
print("Insertion Sort")
print(insertionSort(unSortedList2))



def bubbleSort(arr):
    
    arrLength = len(arr)
    
    for i in range(arrLength):
        
        swapped = False
        
        for j in range(0 , arrLength - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] , arr[j + 1] , arr[j]
                swapped = True
        if not swapped:
            break
        
        return arr
    


unSortedList3 = [5, 7, 9, 2, 1, 8, 4, 6, 3]
print('--------------------------')
print("Insertion Sort")
print(insertionSort(unSortedList))



def mergeSort(arr):
    
    arrLength = len(arr)
    
    if arrLength <= 1:
        return arr
    
    mid = arrLength // 2
    l_half = arr[:mid]
    r_half = arr[mid:]
    l_half = mergeSort(l_half)
    r_half = mergeSort(r_half)
    return merge(l_half , r_half)
    
    
def merge(left , right):
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
            





unSortedList4 = [5, 7, 9, 2, 1, 8, 4, 6, 3]
print('--------------------------')
print("Merge Sort")
print(mergeSort(unSortedList4))