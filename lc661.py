class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        import math
        m = len(M)
        if m == 0:
            return []

        n = len(M[0])

        ret = [[None]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = 0
                currSum = 0
                for ii in [-1,0,1]:
                    if i+ii<0 or i+ii>=m:
                        continue
                    for jj in [-1,0,1]:
                        if j+jj<0 or j+jj>=n:
                            continue
                        count += 1
                        currSum += M[i+ii][j+jj]
                ret[i][j] = math.floor(currSum/count)

        return ret