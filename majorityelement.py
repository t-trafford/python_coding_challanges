nums = [3,2,3]

def majorityElement(nums):
    ans = {}
    averg = (len(nums)/2)
    temp = []
    for i in range(len(nums)):
        if nums[i] not in ans:
            ans[nums[i]] = 1
        else:
            ans[nums[i]]+=1
    last = 0

    for k,v in ans.items():
        if v > averg and v > last:
            last = v
            temp.append(k)

    return temp[-1]

x = majorityElement(nums)
print(x)