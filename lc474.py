class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*(n+1) for _ in range(m+1)]
        for string in strs:
            zeros, ones = self._count(string)
            for mm in range(m, zeros-1, -1):
                for nn in range(n, ones-1, -1):
                    dp[mm][nn] = max(dp[mm][nn], 1+dp[mm-zeros][nn-ones])

        return dp[m][n]

    def _count(self, string):
        zeros = 0
        ones = 0
        for c in string:
            if c == '0':
                zeros += 1
            else:
                ones += 1
        return zeros, ones