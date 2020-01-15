nums = [1, 2, 9,3,2,4,7]

def firstmissingele(nums):

    nums.sort()

    for i in range(len(nums)):

        if nums[i] < 0:
            continue

        if nums[i] >= 0 and nums[i]+1 not in nums:
            return nums[i]+1

        if i==len(nums)-1:
            return max(nums)+1


x = firstmissingele(nums)
print(x)

