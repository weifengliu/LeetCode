class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        d1 = 1 # ways at i-2
        d2 = 1 if int(s[0]) >= 1 else 0 # ways at i-1

        for i in range(1, n):
            new = 0
            if int(s[i]) >= 1:
                new += d2

            if 26 >= int(s[i-1:i+1]) >= 10:
                new += d1

            d1 = d2
            d2 = new

        return d2
