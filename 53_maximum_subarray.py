def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int

    """
    #=============================================================
    #  Brute force
    # maxsum = nums[0]
    # for i in range(len(nums)):
    #     cursum = 0
    #     for j in range (i, len(nums)):
    #         cursum+=nums[j]
    #         maxsum = max(cursum, maxsum)

    # return maxsum

    #=============================================================
    # Kadane's algo
    maxsum = submax = nums[0]
    for i in range(1,len(nums)):
        submax = max(nums[i], submax+nums[i])
        maxsum = max(submax, maxsum)
    return maxsum

# test
maxSubArray([-2,1,-3,4,-1,2,1,-5,4])