class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        ret = 0
        i = 2
        while i<=n:
            while n%i == 0:
                ret += i
                n /= i
            i += 1

        return ret


