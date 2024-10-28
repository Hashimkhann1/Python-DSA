


def patteren():
    for star in range(1,6):
        print('*' * star)


patteren()


# //////////////// Question 1 ////////////////

# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

def question1():
    n = 5
    
    # method 1
    for i in range(n):
        print('* ' * n)
    
    # method 2
    # for i in range(1 , 6):
    #     for j in range(1,6):
    #         print("*", end=" ")
    #     print()
    
        
# question1()


# //////////////// Question 2 ////////////////

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

def question2():
    n = 6
    
    # Method 1
    # for i in range(1, n):
        # print('* ' * i )
    
    # Method 2
    for i in range(1 , n):
        for j in range(1 , i + 1):
            print('*' , end=' ')
        print()

# question2()


# //////////////// Question 3 ////////////////

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 


def question3():
    n = 6
    for i in range(1, n):
        print('* ' * (n - i))


# question3()


# //////////////// Question 4 ////////////////

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 


def question4():
    
    for i in range(1 , 6):
        for j in range(1 , i + 1):
            print(j , end=" ")
        print()


# question4()

# //////////////// Question 5 ////////////////

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1 

def question5():
    n = 5
    for i in range(n , 0 , -1):
        for j in range(i , 0 , -1):
            print(j , end=' ')
        print()


# question5()


# //////////////// Question 6 ////////////////

#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 

def question6():
    
    n = 5
    for i in range(1 , n + 1):
        print(" " * (n - i) , end=' ')
        print("* " * i)


# question6()


# //////////////// Question 7 ////////////////

#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * * 
#  * * * * * * 
#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       * 


def question7():
    n = 6
    
    for i in range(1 , n + 1):
        print(" " * (n - i) , end=' ')
        print("* " * i)
    
    for j in range(n - 1 , 0 , -1):
        print(" " * (n - j) , end=' ')
        print("* " * j)
        


# question7()
    


