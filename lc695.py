class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        m = len(grid)
        if m == 0:
            return maxArea

        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                currArea = self._helper(grid, visited, i, j, m, n)
                maxArea = max(maxArea, currArea)

        return maxArea

    def _helper(self, grid, visited, i, j, m, n):
        if i<0 or i>=m or j<0 or j>=n or visited[i][j]:
            return 0

        currArea = 0
        visited[i][j] = True
        if grid[i][j] != 0:
            currArea += 1
            currArea += self._helper(grid, visited, i-1, j, m, n)
            currArea += self._helper(grid, visited, i, j-1, m, n)
            currArea += self._helper(grid, visited, i, j+1, m, n)
            currArea += self._helper(grid, visited, i+1, j, m, n)

        return currArea
