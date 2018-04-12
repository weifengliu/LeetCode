class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # m*n dimension

        # 0 -> 0: 2
        # 0 -> 1: 3
        # 1 -> 0: 4
        # 1 -> 1: 5
        m = len(board)
        if m == 0:
            return
        else:
            n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.checkWillAlive(board, i, j, m, n) and board[i][j]==0:
                    board[i][j] = 3
                elif self.checkWillAlive(board, i, j, m, n) and board[i][j]==1:
                    board[i][j] = 5
                elif (not self.checkWillAlive(board, i, j, m, n))and board[i][j]==0:
                    board[i][j] = 2
                else:
                    board[i][j] = 4

        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] % 2

        return

    def checkWillAlive(self, board, i, j, m, n):
        count = 0
        for (ii,jj) in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
            if ii<0 or jj<0 or ii>=m or jj>=n:
                continue
            else:
                if board[ii][jj] == 1 or board[ii][jj]>=4:
                    count += 1

        if board[i][j]==0:
            return count==3
        else:
            return count in (2,3)
