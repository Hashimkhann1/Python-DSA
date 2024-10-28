



def selectionSort(arr):
    
    n = len(arr)
    
    for i in range(n):

        min_index  = i
        
        for j in range(i + 1 , n):
            if arr[j] < arr[min_index]:
                
                min_index = j
            
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
    
    return arr
    




unSortedList = [1000, 20000, 500, 2500, 100, 15000]
print(selectionSort(unSortedList))
print('------------------------')


def insertionSort(arr):
    
    arrLength = len(arr)
    
    for i in range(arrLength):
        
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            print(type(key))
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        
    return arr


print(insertionSort(unSortedList))