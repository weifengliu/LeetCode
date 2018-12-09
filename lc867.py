class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = None
        m = len(A)
        if m > 0:
            n = len(A[0])
        ret = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ret[j][i] = A[i][j]

        return ret
