s = "I"

def intToRoman(s):
    d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
         4: 'IV', 1: 'I'}
    res = 0
    for k,v in d.items():
        while len(s)>0:
            res += k
            s = s.replace(v, '')

    return res
x = intToRoman(s)
print(x)
