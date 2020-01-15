
nums = [5,4,3,2,1]
def findUnsortedSubarray(nums):
    # start = 0
    # end = 0
    # count = 0
    #
    # if len(nums) < 2 or nums ==sorted(nums):
    #     return 0
    # if len(nums) ==2 and nums[0]>nums[1]:
    #     return 2
    #
    # for i in range(len(nums)):
    #     if i == len(nums)-1 and count==1 and end==0:
    #         end = start+2
    #     elif i == len(nums)-1:
    #         break
    #     else:
    #         # print(i)
    #         if nums[i] >= nums[i + 1] and start == 0 and count==0:
    #             start = i
    #             count +=1
    #         elif nums[i] >= nums[i + 1] and end < i + 2:
    #             end = i + 2
    #
    # return end - start

    check = sorted(nums)
    temp = []

    for i in range(len(nums)):
        if nums[i] != check[i]:
            temp.append(i)

    if len(temp)==0:
        return 0
    else:
        return max(temp)-min(temp)+1

x = findUnsortedSubarray(nums)
print(x)