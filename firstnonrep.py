import timeit

s = "loveleetcode"


def firstUniqChar(s):
    d = {}
    for c in s:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1

    for i in range(len(s)):
        c = s[i]
        if d[c] == 1:
            return i

    return -1
x = firstUniqChar(s)
print(x)
