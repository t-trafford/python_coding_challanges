
n = 5
x = {1,3,5}


def stair_way(n, x):

    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    print(cache)

    #
    #
    # elif cache[n] != None:
    #     return cache[n]


    for j in range(1,n+1):
        # c = [k for k in x if j - k >= 0]
        # print(c)
        # cache[j] += sum(cache[j - h] for h in c)
        cache[j] += sum(cache[j - k] for k in x if j - k >= 0)
    return cache[n]


p = stair_way(n, x)
print(p)