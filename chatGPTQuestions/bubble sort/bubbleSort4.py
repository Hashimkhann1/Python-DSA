

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



unSortedList = [70, 85, 62, 90, 75, 50, 100]
print(bubbleSort(unSortedList))
print('-------------------------')
print('Insertion Sort')


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

        

print(insertionSort(unSortedList))
print('-------------------------')
print("Selection sort")


def selectionSort(arr):
    
    arrLength = len(arr)
    
    for i in range(arrLength):
        
        min_index = i
        
        for j in range(i + 1 , arrLength):
            
            if arr[j] > arr[min_index]:
                
                min_index = j
        
        arr[j] , arr[min_index] = arr[min_index] , arr[j]
    return arr


print(selectionSort(unSortedList))
# [70, 85, 62, 90, 75, 50, 100]


