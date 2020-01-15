strs = ["fliw","grow","crow"]

def lc_prefix(strs):


        if strs == []:
            return ""
        elif len(strs) == 1:
            return strs[0]
        prefix = strs[1]
        for i in range(0, len(strs)):
            while not strs[i].endswith(prefix):
                prefix = prefix[1:]
                # print(prefix)
        return prefix

x = lc_prefix(strs)
print(x)

lc_prefix(strs)
