class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n==0:
            return 0
        if n<=2:
            return min(cost)
        totalCost = [0]*n
        totalCost[0:2] = cost[0:2]
        for i in range(2, n):
            totalCost[i] = cost[i] + min(totalCost[i-1], totalCost[i-2])

        return min(totalCost[-2:])
