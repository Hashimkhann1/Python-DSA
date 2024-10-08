


num = int(input("Enter any number to find factorial!"))

print(num);

factorial = num

while num > 1:
    num = num - 1
    factorial *= num
    
print(factorial)