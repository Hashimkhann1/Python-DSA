
def findTheMaXSumSlidingWindow(window , arr):
    current = 0
    for i in range(window):
        current += arr[i]
    
    maxx = current
        
    for i in range(1, len(arr) - window + 1):
        current = current - arr[i - 1] + arr[i + window - 1]
        if current > maxx:
            maxx = current
    
    return maxx
    
    



list1 = [3,8,2,5,7,6,12]
w = 4
print(findTheMaXSumSlidingWindow(w , list1))