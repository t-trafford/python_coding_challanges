n = 66
def power3(n):
    if n < 3:
        return False
    while n % 3 == 0:
        n = n/3
        return True

    return False

x = power3(n)
print(x)


