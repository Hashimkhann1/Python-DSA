


def bubbleSort(arr):
    
    arrLength = len(arr)
    
    for i in range(arrLength):
        swapped = False
        
        for j in range(0 , arrLength - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]
                swapped = True
                print(arr)

        if not swapped:
            break
        
    return arr



unSortedList = [5, 1, 4, 2, 8]
print(bubbleSort(unSortedList))