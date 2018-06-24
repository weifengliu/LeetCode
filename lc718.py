class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        maxLen = 0
        m = len(A)
        n = len(B)
        dp = [ [0]*n for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i-1][j-1]
                maxLen = max(maxLen, dp[i][j])

        return maxLen