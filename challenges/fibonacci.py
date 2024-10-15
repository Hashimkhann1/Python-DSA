




def getFebonacciNumbers(numberRange):
    fibonacciNumbersList = [0,1]
    
    while True:
        
        next_fib = fibonacciNumbersList[-2] + fibonacciNumbersList[-1]
        
        if next_fib > numberRange:
            break
        else:
            fibonacciNumbersList.append(next_fib)
            
    return fibonacciNumbersList
            

numbersRange = int(input("Enter any reange of number to find the febonacci seriese: "))
print(getFebonacciNumbers(numbersRange))