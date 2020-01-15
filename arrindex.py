

num = [1,3,5,6]
val = 0
# CMXLIV

j = 0

def arrindex(num, val):
    j = 0
    for i in range(len(num)):

        if val > num[i]:

            j += 1

    return j

X = arrindex(num, val)
print(X)

