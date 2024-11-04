
def selectionSort(lis):
    
    lisLength = len(lis)
    
    for i in range(lisLength):
        
        min_index = i
        
        for j in range(i + 1 , lisLength):
            if lis[j] < lis[min_index]:
                min_index = j
                
        lis[i] , lis[min_index] = lis[min_index] , lis[i]
    
    return lis
    
    

unSortedList = [48, 88, 10, 84, 1, 4, 92, 50, 70, 34]
print(selectionSort(unSortedList))



def insertionSort(lis):
    
    lisLength = len(lis)
    
    for i in range(lisLength):
        
        key = lis[i]
        j = i - 1
        
        while i >= 0 and key < lis[j]:
            
            lis[j + 1] = lis[j]
            i -= 1
        lis[j + 1] = key
    
    return lis



unSortedList1 = [48, 88, 10, 84, 1, 4, 92, 50, 70, 34]
print('----------------------------')
print("Insertion Sort")
print(insertionSort(unSortedList))


def bubbleSort(lis):
    
    lisLength = len(lis)
    
    for i in range(lisLength):
        
        swapped = False
        
        for j in range(0 , lisLength - i - 1):
            
            if lis[j] > lis[j + 1]:
                lis[j] , lis[j + 1] = lis[j + 1] , lis[j]
            
        if not swapped:
            break
        
    return lis
    
    
unSortedList2 = [48, 88, 10, 84, 1, 4, 92, 50, 70, 34]
print('----------------------------')
print("Bubble Sort")
print(bubbleSort(unSortedList))



def mergeSortDivide(lis):
    
    lisLength = len(lis)
    
    if lisLength <= 1:
        return lis
    
    mid = lisLength // 2
    
    l_half = lis[:mid]
    r_half = lis[mid:]
    
    l_half = mergeSortDivide(l_half)
    r_half = mergeSortDivide(r_half)
    
    return mergeConqure(l_half , r_half)


def mergeConqure(left , right):
    
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


unSortedList3 = [48, 88, 10, 84, 1, 4, 92, 50, 70, 34]
print('----------------------------')
print("Merge Sort")
print(mergeSortDivide(unSortedList3))