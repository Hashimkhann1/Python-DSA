


def lowestNumberInList(lis):
    
    minVal = lis[0]
    
    for i in range(1 , len(lis)):
        if lis[i] < minVal:
            minVal = lis[i]
    
    return minVal


lis = [7, 12, 9, 4, 11 , 100 , 3 , 40 , 1]
print(lowestNumberInList(lis))