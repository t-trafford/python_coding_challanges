nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):

    a = []
    b = set()

    for i in range(len(nums)):

        if nums[i] not in b:
            a.append(nums[i])
            b.add(nums[i])

        else:
            b.add(nums[i])

    return a

X = removeDuplicates(nums)
print(X)