class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        allowance = 0
        prev = False
        for i in range(len(flowerbed)):
            if flowerbed[i]==1:
                prev = True
                continue

            if (i==0 or (not prev)) and \
                    (i == len(flowerbed)-1 or flowerbed[i+1]==0):
                allowance += 1
                prev = True
            else:
                prev = False

        return allowance>=n