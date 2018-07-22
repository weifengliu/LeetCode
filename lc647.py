class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        total = 0
        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(i+1):
                if i == j:
                    dp[j][i] = 1
                else:
                    if s[i] == s[j]:
                        if i-j > 1:
                            dp[j][i] = dp[j+1][i-1]
                        else:
                            dp[j][i] = 1

                total += dp[j][i]

        return total