a = [1,2,-1,-1]
def threeSum(a):
    result = []
    sub_result = []
    final = []
    c = set()
    j = 0
    i=0
    p=3
    k=0

    if a == [0, 0, 0]:
        return [[0, 0, 0]]

    for i in range(i, len(a)-1):

        j += 1

        for j in range(j, len(a)):

            fs = a[i] + a[j]
            target = 0 - fs

            if target in a:
                if a.index(a[i]) != a.index(a[j]) and a.index(a[j]) != a.index(target) and a.index(a[i])!= a.index(target):
                    sub_result = [a[i], a[j], target]
                    uniq = all(elem in result for elem in sub_result)
                    print("sub",sub_result)
                    if not uniq:
                        result += sub_result
                    print("res", result)



                        # # print(a[i])
                        # sub_result.append()
                        # # print(a[j])
                    # sub_result.append(target)

        i+=1
    while p <= len(result):
            final += [result[k:p]]
            k+=3
            p+=3
    return final

x = threeSum(a)
print(x)