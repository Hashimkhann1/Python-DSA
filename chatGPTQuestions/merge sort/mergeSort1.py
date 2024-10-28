


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



unSortedList = [60 , 20 , 40 , 10 , 90 , 30 , 80 , 50]
print(mergeSort(unSortedList))


