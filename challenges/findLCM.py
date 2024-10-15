

number1 = int(input("Enter first number for LCM: "))
number2 = int(input("Enter second number for LCM: "))

maxNum = max(number1 , number2)


while True:
    if maxNum % number1 == 0 and maxNum % number2 == 0:
        break
    else:
        maxNum += 1

print(f"The LCM of {number1} and {number2} is {maxNum}")