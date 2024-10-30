

def divide(arr):
    
    arrLength = len(arr)
    
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if arrLength <= 1:
        return arr
    
    # Split the array into halves
    mid = arrLength // 2
    l_half = arr[:mid]
    r_half = arr[mid:]
    
    # Recursively divide the halves
    l_half = divide(l_half)
    r_half = divide(r_half)
    
    # Conquer (merge) the sorted halves
    return conquer(l_half , r_half)

def conquer(left , right):
    
    new = []
    leftIndex , rightIndex = 0 , 0
    
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            new.append(left[leftIndex])
            leftIndex += 1
        else:
            new.append(right[rightIndex])
            rightIndex += 1
    
    new.extend(left[leftIndex:])
    new.extend(right[rightIndex:])
    
    return new

    


unSortedList = [38, 27, 43, 3, 9, 82, 10]
print(divide(unSortedList))



def selectionSortt(arr):
    
    arrLength = len(arr)
    
    for i in range(arrLength):
        
        min_index = i
        
        for j in range(i + 1 , arrLength):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
        
    return arr
            

unSortedList1 = [38, 27, 43, 3, 9, 82, 10]
print("---------------------------")
print("Selection Sort")
print(selectionSortt(unSortedList1))


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



unSortedList2 = [38, 27, 43, 3, 9, 82, 10]
print("---------------------------")
print("Insertion Sort")
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
        
        



unSortedList3 = [38, 27, 43, 3, 9, 82, 10]
print(bubbleSort(unSortedList3))