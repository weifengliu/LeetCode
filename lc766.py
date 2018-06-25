class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        prevRow = matrix[0]
        for i in range(1, m):
            if matrix[i][1:] != prevRow[:-1]:
                return False
            prevRow = matrix[i]

        return True