

class Solution(object):
    def getSneakyNumbers(self, nums):

        count = 0
        duplicateNum = []
        
        for num in nums:

            for x in nums:
                
                if x == num:
                    count += 1
                    if count == 2:
                        if x not in duplicateNum:
                            duplicateNum.append(x)
                        break
            count = 0
        duplicateNum.sort()
        return duplicateNum




digitVilla = Solution()
# print(digitVilla.getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2]))



def checkDup(nums):
    dup = []
    containNum = []

    for num in nums:
        
        if num not in containNum:
            containNum.append(num)
        else:
            dup.append(num)
            print(dup)




checkDup([7,1,5,4,3,4,6,0,9,5,8,2])