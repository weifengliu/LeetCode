class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [[2] * n for _ in range(n)]
        pos = {A[i]: i for i in range(n)}
        res = 2

        for i in range(2, n):
            for j in range(i - 1, 0, -1):
                prev = A[i] - A[j]
                if prev >= A[j]:
                    break
                else:
                    if prev in pos:
                        dp[j][i] = max(dp[j][i], dp[pos[prev]][j] + 1)
                        res = max(res, dp[j][i])

        return res if res > 2 else 0