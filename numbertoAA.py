class Solution(object):
    n = 52

    def convertToTitle(n):
        """
        :type n: int
        :rtype: str
        """
        dict = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13,
                'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22,
                'y': 25, 'x': 24, 'z': 26}
        l1 = []
        if n < 1:
            return None
        else:
            while n > 0:
                dig_val = n % 26
                n = n - dig_val
                if dig_val > 0:
                    for name, age in dict.items():
                        if age == dig_val:
                            l1.append(name)
                else:
                    n = n / 26

            ans = ''.join(reversed(l1)).upper()
            return ans

    x = convertToTitle(n)
    print(x)

    convertToTitle(n)