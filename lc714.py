class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if n==0:
            return 0

        s0 = 0 #no stock at this moment
        s1 = -prices[0]-fee #hold 1 stock at this moment

        for i in range(1, n):
            s0 = max(s0, s1+prices[i])
            s1 = max(s1, s0-prices[i]-fee)

        return s0