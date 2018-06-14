class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        [max3, max2, max1] = [-1001] * 3
        [min2, min1] = [1001] * 2

        for num in nums:
            if num > max3:
                max1 = max2
                max2 = max3
                max3 = num
            elif num > max2:
                max1 = max2
                max2 = num
            elif num > max1:
                max1 = num

            if num < min2:
                min1 = min2
                min2 = num
            elif num < min1:
                min1 = num

        return max(max3 * max2 * max1, max3 * min1 * min2)