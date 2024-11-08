

def mergeSortedArrayBySelectionSort(arr1 , arr2 , m , n):
    
    arr1[m:] = arr2
    
    arr1Length= len(arr1)
    
    for i in range(arr1Length):
        
        min_index = i
        
        for j in range(i + 1 , arr1Length):
            
            if arr1[j] < arr1[min_index]:
                min_index = j

        arr1[i] , arr1[min_index] = arr1[min_index] , arr1[i]
            
    
    return arr1
        
        

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(mergeSortedArrayBySelectionSort(nums1 , nums2 , m , n))
print('------------------------------')
print("Insertion Sort")


def mergeSortedArrayByInsertionSort(arr3 , arr4 , m , n):
    
    arr3[m : ] = arr4
    
    arr3Length = len(arr3)
    
    for i in range(1 , arr3Length):
        
        key = arr3[i]
        j = i - 1
        
        while i >= 0 and key < arr3[j]:
            arr3[j + 1] = arr3[j]
            j -= 1
        arr3[j + 1] = key
    
    return arr3




num3 = [1,2,3,0,0,0]
nums4 = [2,5,6]
print(mergeSortedArrayByInsertionSort(num3 , nums4 , m , n))
print('------------------------------')
print("Bubble Sort")



def mergeSortedArrayByBubbleSort(arr5 , arr6 , m , n):
    
    arr5[m:] = arr6
    arr5Length = len(arr5)
    
    for i in range(arr5Length):
        
        swapped = False
        
        for j in range(0 , arr5Length - i - 1):
            if arr5[j] > arr5[j + 1]:
                arr5[j] , arr5[j + 1] = arr5[j + 1] , arr5[j]
                swapped = True
        
        if not swapped:
            break
        
    return arr5


num5 = [1,2,3,0,0,0]
nums6 = [2,5,6]
print(mergeSortedArrayByBubbleSort(num5 , nums6 , m , n))