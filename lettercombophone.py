digits = '23'

def letterCombinations(digits):

    ans = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
    temp = []
    for d in digits:
        if d in ans:
            temp.append(ans[d].split())

    return temp

    # for i in range(len(temp))


x= letterCombinations(digits)
print(x)