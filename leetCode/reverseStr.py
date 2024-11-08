
s = ["h","e","l","l","o"]

def reverseString(s):

    # /////// soluion One ///////

    # s.reverse()
    # print(s)

    # /////// Solution Two /////// but i create anther list

    # ans = []
    # for i in range(len(s)):
    #     ans.append(s[(len(s) - 1) - i])
    # print(ans)


    # ///////  Solution Three ///////
    left , right = 0, len(s) - 1

    while left < right:

        s[left] , s[right] = s[right] , s[left]
        print(s)
        
        left += 1
        right -= 1

        # print(left)
        # print(right)
    

reverseString(s)