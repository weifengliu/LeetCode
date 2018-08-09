class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        cost = [None]*n
        cost[src] = 0
        for _ in range(K+1):
            prev = list(cost)
            for (a, b, fee) in flights:
                if prev[a] is not None and cost[b] is not None:
                    cost[b] = min(cost[b], prev[a]+fee)
                else:
                    if prev[a] is not None:
                        cost[b] = prev[a]+fee

        return cost[dst] if cost[dst] is not None else -1