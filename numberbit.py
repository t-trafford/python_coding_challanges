nums = [1,2,3,1]
x = set()
length = len(nums)
for i in range(0, length):
    if nums[i] in x:
        print("true")
    else:
        x.add(nums[i])
