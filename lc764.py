class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        cache = [[N]*N for _ in range(N)]
        for m in mines:
            cache[m[0]][m[1]] = 0

        for pos in range(N):
            l, r, u, d = 0, 0, 0, 0
            for (i, j) in zip(range(N), reversed(range(N))):
                l = l+1 if cache[pos][i] != 0 else 0
                cache[pos][i] = min(l, cache[pos][i])

                r = r+1 if cache[pos][j] != 0 else 0
                cache[pos][j] = min(r, cache[pos][j])

                u = u+1 if cache[i][pos] != 0 else 0
                cache[i][pos] = min(u, cache[i][pos])

                d = d+1 if cache[j][pos] != 0 else 0
                cache[j][pos] = min(d, cache[j][pos])

        return max([max(r) for r in cache])