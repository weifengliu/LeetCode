class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        import math
        m = len(matrix)
        maxArea = 0
        if m == 0:
            return maxArea

        n = len(matrix[0])
        side = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                side[i][j] = int(matrix[i][j])
                if i > 0 and j > 0:
                    for k in range(side[i-1][j-1]+1):
                        if matrix[i][j-k] == '1' and matrix[i-k][j] == '1':
                            side[i][j] = 1+k
                        else:
                            break
                maxArea = max(maxArea, side[i][j]**2)
        return maxArea


