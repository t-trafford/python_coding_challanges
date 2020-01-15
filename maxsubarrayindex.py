
nums= [2,-100,-7,8,3,-2, 33,99,-88]

def maxSubArray(nums):

    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    end = nums.index(max(nums))
    # print("end of index", end)
    print(nums)

    start = len(nums)-1
    for j in range(len(nums)-1, 0, -1):

        if nums[j-1] > 0 and j==0:
            start = 0

        if nums[j-1] < 0:
            break

        if nums[j-1] > 0:
            start -=1

    return start, end, max(nums)






    # return max(nums)




x = maxSubArray(nums)
print(x)