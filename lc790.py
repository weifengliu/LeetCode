class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        D = [0] * (N + 1)
        T = [0] * (N + 1)
        D[1], D[2] = 1, 2
        T[1], T[2] = 0, 1

        for k in range(3, N + 1):
            D[k] = D[k - 1] + D[k - 2] + T[k - 1] * 2
            T[k] = D[k - 2] + T[k - 1]

        return D[N]
