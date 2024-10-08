
# ///////// the below is my code withhout any help


# def findGCD(numbers):
    
#     # storig divisorList in it
#     bothNumberDivisors = {}

#     # looping for both numbers
#     for num in numbers.split(','):
#         divisorList = []

#         # finding divisors of the number
#         for i in range(1,int(num) + 1):
#             if int(num) % i == 0:
#                 # adding in the list
#                 divisorList.append(i)
#         # adding in divisor list of number in bothNumberDivisors
#         bothNumberDivisors[num] = divisorList


#     commonDivisros = []

#     # finding common divisor and storing in commonDivisros
#     for i in bothNumberDivisors[numbers.split(',')[0]]:
#         if(i in bothNumberDivisors[numbers.split(',')[1]]):
#            commonDivisros.append(i)

#     # Sorting the commonDivisor list
#     commonDivisros.sort()
#     return commonDivisros[-1]
    
        

# num = input("Enter any two numbers to find it's GDC! like 10,20 ::> ")
# print(findGCD(num))



# //// Below is the chatGPT code.


def findGCD(numbers):

    # // Splitting the input once and storing it
    num1 , num2 = map(int, numbers.split(','))
    
    # // Function to find divisors of a number
    def findDivisors(num):
        return [i for i in range(1, num + 1) if num % i == 0]
    

    # // Finding divisors for both numbers
    divisors1 = findDivisors(num1)
    divisors2 = findDivisors(num2)

    # // Finding common divisors by set intersection
    commonDivisors = list(set(divisors1) & set(divisors2))

    # // Returning the greatest common divisor
    return max(commonDivisors)


# // Get input from the user
num = input("Enter any two numbers to find it's GDC! like 10,20 ::> ")
print(findGCD(num))