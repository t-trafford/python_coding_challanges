
n=5

def climbstair(n):



    if n == 0:
        return 0

    if n ==1:
        return 1

    if n ==2:
        return 2

    else:
            result = climbstair(n-1) + climbstair(n-2)


    return result

X = climbstair(n)
print(X)

