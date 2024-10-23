

def merge(nums1, m, nums2, n):

    # /////// solution 1 ///////

    # n = len(nums1) - m

    # for i in range(n):
    #     nums1.pop()
    # nums1.extend(nums2)
    # nums1.sort()
    # print(nums1)

    # ///// solution 2 ///////

    for i in range(n):
        nums1[m + i] = nums2[i]
    nums1.sort()

    print(nums1)




# s = Solution()

merge([1,2,3,0,0,0], 3 ,[2,5,6] , 3)