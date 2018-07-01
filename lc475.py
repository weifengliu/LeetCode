class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        amount = [[0]*(n+1) for _ in range(n+1)]

        for s in range(n, 0, -1):
            for e in range(s+1, n+1):
                amount[s][e] = min([ x + max(amount[s][x-1], amount[x+1][e]) for x in range(s, e)])

        return amount[1][n]