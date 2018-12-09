class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        m = len(grid)
        if m > 0:
            n = len(grid[0])
        for i in range(m - 2):
            for j in range(n - 2):
                if self.isMagic(i, j, grid):
                    count += 1

        return count

    def isMagic(self, i, j, grid):
        counter = [0] * 9
        for ii in range(i, i + 3):
            for jj in range(j, j + 3):
                if grid[ii][jj] == 0 or grid[ii][jj] > 9:
                    return False
                counter[grid[ii][jj] - 1] = 1
        if sum(counter) != 9:
            return False

        if sum(grid[i][j:j + 3]) != 15 or sum(grid[i + 1][j:j + 3]) != 15 or sum(grid[i + 2][j:j + 3]) != 15:
            return False

        if grid[i][j] + grid[i + 1][j] + grid[i + 2][j] != 15 or grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][
            j + 1] != 15 or grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2] != 15:
            return False

        if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != 15 or grid[i][j + 2] + grid[i + 1][j + 1] + \
                grid[i + 2][j] != 15:
            return False

        return True
