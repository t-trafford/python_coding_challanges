
s = "BZ"

val = 0
for i in range(0, len(s)):
    chVal = ord(s[i]) - ord('A') + 1
    power = pow(26, len(s) - 1 - i)
    val += chVal * power
print(val)