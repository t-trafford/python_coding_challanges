s = "pwwkew"

def lengthOfLongestSubstring(s):
    result = 0
    temp = []
    for item in s:
        if item in temp:
            if len(temp) > result:
                result = len(temp)
            temp = temp[temp.index(item) + 1:]
            temp.append(item)
        else:
            temp.append(item)
    return max(len(temp), result)
    # return temp


x = lengthOfLongestSubstring(s)
print(x)

