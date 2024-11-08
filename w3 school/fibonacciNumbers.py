

def findFibonacciNumbers(runTimes):
    
    prev1 = 0
    prev2 = 1
    
    for fib in range(runTimes):
        
        new_fib = prev1 + prev2
        print(f'From for loop {new_fib}')
        prev1 = prev2
        prev2 = new_fib
    
    
runTiemNumber = int(input("How much times you want to run the loop to print the Fibonacci numbers: "))
findFibonacciNumbers(runTiemNumber)



print("-----------------------")
print("-----------------------")
print("-----------------------")


count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(f"From recursion {newFibo}")
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)