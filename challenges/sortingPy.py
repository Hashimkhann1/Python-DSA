




def sortList(arr):
    
    for i in range(len(arr)):
        for j in range(i + 1 , len(arr)):
          if arr[i] > arr[j]:
              x = arr[i]
              arr[i] = arr[j]
              arr[j] = x
    print('--------------------------')          
    return arr           
           
    


    
unSortedList = [10,4,30,20,15,3,8,5,9,2]
# print(sortList(unSortedList))


def max_chocolate(money, price_per_chocolate, wrappers_needed_for_chocolate):
    chocolate = money // price_per_chocolate
    wrappers = chocolate
    
    while wrappers >= wrappers_needed_for_chocolate:
        new_chocolates = wrappers // wrappers_needed_for_chocolate
        chocolate += new_chocolates
        wrappers = new_chocolates + (wrappers % wrappers_needed_for_chocolate)
    
    return chocolate
    
    


# given values
money = int(input("Enter how many rupeees you have: "))
price_per_chocolate = 1
wrappers_nedded_for_chocolate = 3

print(max_chocolate(money , price_per_chocolate , wrappers_nedded_for_chocolate))







# from CHATGPT


# def max_chocolates(money, price_per_chocolate, wrappers_needed_for_chocolate):
#     chocolates = money // price_per_chocolate
#     wrappers = chocolates

#     while wrappers >= wrappers_needed_for_chocolate:
#         new_chocolates = wrappers // wrappers_needed_for_chocolate
#         chocolates += new_chocolates
#         wrappers = new_chocolates + (wrappers % wrappers_needed_for_chocolate)

#     return chocolates

# # Given values
# money = 15
# price_per_chocolate = 1
# wrappers_needed_for_chocolate = 3

# # Calculate the maximum chocolates that can be eaten
# max_chocolates_eaten = max_chocolates(money, price_per_chocolate, wrappers_needed_for_chocolate)
# max_chocolates_eaten
