
s = "CMLXIII" # CMXLIV


def romtoint(s):

    D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    for k,v in D.items():

        while i < len(s):
            if i == len(s)-1:
                result += D[s[i]]
                i+=1
            elif D[s[i]] < D[s[i+1]]:
                result += (D[s[i+1]]-D[s[i]])
                i +=2
            else:
                result += D[s[i]]
                i +=1
    return result


x = romtoint(s)
print(x)