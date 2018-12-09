class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        n = len(candies)
        d = {}
        for candy in candies:
            if candy not in d:
                d[candy] = 0
            d[candy] += 1

        return min(len(d.keys()), n/2)