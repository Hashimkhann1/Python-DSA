


def quickSort(arr , low , high):
    
    if low < high:
        
       pivot = partition(arr , low , high)
       quickSort(arr , low , pivot - 1)
       quickSort(arr , pivot + 1 , high)
        
        
def partition(arr , low , high):
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low , high):
        if arr[j] < pivot:
            i += 1
            print(f' J >>> {j}')
            print(f' I >>>>> {i}')
            temp = arr[i]
            print(temp)
            arr[i] = arr[j]
            arr[j] = temp
    
    i += 1
    temp = arr[i]
    print(f'Outer temp {temp}')
    arr[i] = pivot
    arr[high] = temp
    
    return i
    




unSortedList = [6,3,9,5,2,8]
n = len(unSortedList)
quickSort(unSortedList , 0 , n - 1)
print(unSortedList)