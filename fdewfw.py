


s = "(12(34))"

def balance_paren(s):

    match = "()"
    open_paren = '('
    close_paren = ')'
    stack = []


    for i in range(len(s)):

        if s[i] == open_paren:
            stack.append(s[i])

        elif s[i] == close_paren:

            if len(stack) ==0:
                return False
            else:
               if stack.pop()+s[i] != match:
                   return False

    if len(stack) != 0:
        return False
    else:
        return True


x = balance_paren(s)
print(x)





