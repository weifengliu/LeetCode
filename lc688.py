class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if K == 0:
            return 1

        curr = [[0]*N for _ in range(N)]
        curr[r][c] = 1
        for step in range(K):
            prev = curr
            curr = [[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    if prev[i][j] != 0:
                        for direction in [(-1, -2), (-2,-1), (-2,1),
                                          (-1,2), (1,2), (2,1), (2,-1), (1,-2)]:
                            rr, cc = i+direction[0], j+direction[1]
                            if 0<=rr<N and 0<=cc<N:
                                curr[rr][cc] += 0.125*prev[i][j]

        return sum([sum(x) for x in curr])