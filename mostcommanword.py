
import re
import operator
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mostCommonWord(paragraph, banned):

    paragraph = paragraph.lower()
    paragraph = re.findall(r"\w+", paragraph)
    ans = {}
    for i in range(len(paragraph)):

        if paragraph[i] not in banned and paragraph[i] not in ans:
            ans[paragraph[i]] = 1
        if paragraph[i] not in banned and paragraph[i] in ans:
            ans[paragraph[i]] += 1
    return max(ans.items(), key=operator.itemgetter(1))[0]

x = mostCommonWord(paragraph, banned)
print(x)