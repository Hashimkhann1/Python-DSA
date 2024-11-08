
def selectionSort(lis):
    lisLength = len(lis)
    
    for i in range(lisLength):
        
        min_index = i
        
        for j in range(i + 1 , lisLength):
            
            if lis[j] < lis[min_index]:
                min_index = j
                
        lis[i] , lis[min_index] = lis[min_index] , lis[i]
    
    return lis



unSortedList = [1000, 20000, 500, 2500, 100, 15000]
print(selectionSort(unSortedList))


def insertionSort(lis):
    
    lisLength = len(lis)
    
    for i in range(1 , lisLength):
        
        key = lis[i]
        j = j - 1
        
        while j >= 0 and key < lis[j]:
            lis[j + 1] = lis[j]
            j -= 1
        lis[j + 1] = key
    return lis


unSortedList1 = [1000, 20000, 500, 2500, 100, 15000]
print("--------------------")
print("Insertion Sort")
print(selectionSort(unSortedList1))


def bubbleSort(lis):
    lisLength = len(lis)
    
    for i in range(lisLength):
        swapped = False
        
        for j in range(0 , lisLength - i - 1):
            
            if lis[j] > lis[j + 1]:
                lis[j] , lis[j + 1] = lis[j + 1] , lis[j]
                swapped = True
        if not swapped:
            break
    return lis




unSortedList2 = [1000, 20000, 500, 2500, 100, 15000]
print("---------------------")
print("Bubble Sort")
print(bubbleSort(unSortedList2))


def mergeSortDivide(lis):
    
    lisLength = len(lis)
    
    if lisLength <= 1:
        return lis
    
    mid = lisLength // 2
    l_half = lis[:mid]
    r_half = lis[mid:]
    l_half = mergeSortDivide(l_half)
    r_half = mergeSortDivide(r_half)
    
    return mergeSortConqure(l_half , r_half)


def  mergeSortConqure(left , right):
    
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




unSortedList3 = [1000, 20000, 500, 2500, 100, 15000]
print("---------------------")
print("Merge sort")
print(mergeSortDivide(unSortedList3))



def quickSort(lis , low , high):
    
    if low < high:
        pidx = partition(lis , low , high)
        quickSort(lis , low , pidx - 1)
        quickSort(lis , pidx + 1 , high)
        
        
        return lis

def partition(lis , low , high):
    
    i = low - 1
    
    for j in range(low , high):
        
        if lis[j] < lis[high]:
            i += 1
            lis[i] , lis[j] = lis[j] , lis[i]
    i += 1
    lis[i] , lis[high] = lis[high] , lis[i]
        
    return i
    




unSortedList4 = [1000, 20000, 500, 2500, 100, 15000]
print("---------------------")
print("Quick sort")
n = len(unSortedList4)
print(quickSort(unSortedList4 , 0 , n - 1))
# print(quickSort(unSortedList4 , 0 , n - 1))