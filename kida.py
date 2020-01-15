nofile = 4,
arr = [8,4,6,12]


def permute(nofile, arr):
    arr1 = sorted(arr)
    length = len(arr1)
    count = 0
    # Base Case
    if nofile == 0:
        return 0
    elif length == 0:
        return 0
    else:
         while length >= 0:
             count = count + sum(arr1 [:2])
             arr1 = arr1[2:]
             arr1.insert(0,count)
         return count

x = permute(nofile, arr)
print(x)

permute(nofile, arr)