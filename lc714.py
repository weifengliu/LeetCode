class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        curr = [-prices[0] - fee, 0]  # buy, sell
        for i in range(1, len(prices)):
            prev = list(curr)
            curr[0] = max(prev[0], prev[1] - prices[i] - fee)
            curr[1] = max(prev[1], prev[0] + prices[i])

        return max(curr)