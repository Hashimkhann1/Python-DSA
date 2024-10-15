

def findHCF(numbers):
    
    number1, number2 = map(int , numbers.split(','))

    hcf = 0
    
    for i in range(1,number1 + 1 if number2 > number1 else number2 + 1):
       if number1 % i == 0 and number2 % i == 0:
        hcf = i
    
    return hcf
    
        

numbers = input("Enter any two number to find it's HCF: ")
print(findHCF(numbers))
