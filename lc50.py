class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        absN = abs(n)
        while (absN > 0):
            if absN & 1 == 1:
                res *= x
            absN = absN >> 1
            x *= x

        res = res if n >= 0 else 1.0 / res
        return res