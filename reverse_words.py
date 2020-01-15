s = "  tanay bhatt is great man"



def rev_word(s):
    res = ''
    s = s.lstrip()
    s = s.rstrip()
    # s = ' '.join(s.split())
    while '  ' in s:
        s = s.replace('  ', ' ')

    print(s)
    j = len(s)

    for i in range(len(s)-1,-1,-1):

        if i==0:
            res += s[0:]

        if s[i] == ' ':

            res += s[i+1:] + ' '
            s = s[:i]

    return res


# def rev_word(s):
#
#
#
#     for i in range(len(s)-1,-1,-1):
#
#         if i==0:
#             return s[0:]
#
#
#         # if s[i] == ' ':
#
#         elif s[i] == ' ':
#             return s[i+1:] + ' ' + rev_word(s[0:i])


X = rev_word(s)
print(X)