
string = "johncenahnh"

def isUnique(string):
    l1 = []
    l2 = []

    for c in string:
        if c not in l1:
            l1.append(c)
        else:
            l2.append(c)

    if len(l2) > 0:
      return ''.join(l2)
    else:
        return True


x = isUnique(string)
print (x)

isUnique(string)