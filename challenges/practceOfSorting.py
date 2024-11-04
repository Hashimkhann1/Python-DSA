

def selectionSort(lis):
    
    lisLenght = len(lis)
    
    for i in range(lisLenght):
        
        min_index = i
        
        for j in range(i + 1 , lisLenght):
            
            if lis[j] < lis[min_index]:
                min_index = j
        lis[i] , lis[min_index] = lis[min_index] , lis[i]
        
    return lis


unSortedList0 = [5, 7, 9, 2, 1, 8, 4, 6, 3]
print(selectionSort(unSortedList0))
print('---------------------------')


def insertionSort(lis):
    lisLength = len(lis)
    
    for i in range(1 , lisLength):
        
        key = lis[i]
        j = i - 1
        
        while j >= 0 and key < lis[j]:
            lis[j + 1] = lis[j]
            j -= 1
        lis[j + 1] = key
        
    return lis



unSortedList1 = [5, 7, 9, 2, 1, 8, 4, 6, 3]
print('---------------------------')
print("Insertion Sort")
print(insertionSort(unSortedList1))


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
                


unSortedList2 = [5, 7, 9, 2, 1, 8, 4, 6, 3]
print('---------------------------')
print("Bubble sort")
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
    

unSortedList3 = [5, 7, 9, 2, 1, 8, 4, 6, 3]
print('---------------------------')
print("Merge Sort")
print(mergeSortDivide(unSortedList3))