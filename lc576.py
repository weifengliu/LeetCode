class Solution:
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        paths = [[0]*n for _ in range(m)]

        for remainStep in range(1, N+1):
            prev = [list(paths[x]) for x in range(m)]
            for ii in range(m):
                for jj in range(n):
                    paths[ii][jj] = 0
                    for (x, y) in [(ii-1, jj), (ii+1, jj), (ii, jj-1), (ii, jj+1)]:
                        if m-1 >= x >= 0 and n-1 >= y >= 0:
                            paths[ii][jj] += prev[x][y]
                        else:
                            paths[ii][jj] += 1
                    paths[ii][jj] %= 1000000007

        return paths[i][j]