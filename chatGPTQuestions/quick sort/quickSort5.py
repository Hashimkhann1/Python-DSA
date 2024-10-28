



def quickSort(arr , low , high):
    if low < high:
        pidx = partition(arr , low , high)
        quickSort(arr , low , pidx - 1)
        quickSort(arr , pidx + 1 , high)
    
    return arr
    
    
def partition(arr , low , high):
    
    pivot = arr[low]
    i = low + 1
    
    for j in range(low + 1 , high + 1):
        
        if arr[j] < pivot:
            arr[i] , arr[j] = arr[j] , arr[i]
            i += 1
            
    arr[low] , arr[i - 1] = arr[i - 1] , arr[low]
    
    return i - 1
    
            





unSortedList = [12, 4, 5, 3, 8, 7 , 20, 15, 11, 30, 33, 27]
stringList = ["banana", "apple", "orange", "kiwi", "grape", "mango"]

n = len(unSortedList)
s = len(stringList)
print(quickSort(unSortedList , 0 , n - 1))
print(quickSort(stringList , 0 , s - 1))