
s = "tanay"
#
# def rever(s):
#
#     if len(s) <=1:
#         return s
#
#
#
#     return rever(s[1:]) + s[0]


def rever2(s):

    index = len(s)
    a = []

    if len(s) <=1:
        return s

    else:
        while index > 0:
            a += s[index-1]
            index = index-1

        return ''.join(a)



x = rever2(s)
print(x)

