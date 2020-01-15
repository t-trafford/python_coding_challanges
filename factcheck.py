n = 10


# check if the number is negative, positive or zero
def power3(n):
    factorial = 1
    i = 0
    if n < 0:
        return 0
    elif n == 0:
        return 0
    else:
        for j in range(1,n + 1):
            factorial = factorial*j
        if factorial%10 == 0:
            while factorial%10 == 0:
                factorial = factorial/10
                i = i+1
            return i
        else:
            return 0

x = power3(n)
print(x)

power3(n)