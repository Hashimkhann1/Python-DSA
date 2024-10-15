
# storing all prime number is this list
listOfPrimeNumber = [];

#  checking that number is prime or not
def checkForPrime(num):

    if num < 2:
        return False
    if num == 2:  # 2 is prime
        return True
    if num % 2 == 0:  # Skip even numbers
        return False

    for i in range(3 , num):
        if num % i == 0:
            return False
    else:
        return True



def findPrimeNumber():

    numberToCheck = int(input("Enter a range of numbers to find the prime numbers within the range! "))

    for i in range(2 , numberToCheck):
        if checkForPrime(i):
            listOfPrimeNumber.append(i)
    
    # printng the list of prime numbers
    print(listOfPrimeNumber)

findPrimeNumber()