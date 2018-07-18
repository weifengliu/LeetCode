class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0

        ret = 0
        dp = [[0] * n for _ in range(n)]
        for start in range(n-1, -1, -1):
            dp[start][start] = 1
            for end in range(start+1, n):
                if s[start] == s[end]:
                    dp[start][end] = 2 + dp[start + 1][end - 1]
                else:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

        return dp[0][n-1]