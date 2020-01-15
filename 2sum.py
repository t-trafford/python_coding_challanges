
nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):

        a = set()
        b = []

        for i in range(len(nums)):

            k = target - nums[i]

            if k not in a:
                a.add(nums[i])

            else:
                c = nums.index(k)
                b.insert(0,min(i,c))
                b.insert(1,max(i,c))

        return b

x = twoSum(nums, target)
print(x)

twoSum(nums, target)

