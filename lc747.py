class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return -1

        largeOnes = [nums[0], None]
        largeIdx = 0

        for i in range(1, n):
            if nums[i] > largeOnes[0]:
                largeOnes = [nums[i], largeOnes[0]]
                largeIdx = i
            elif largeOnes[1] is None or nums[i] > largeOnes[1]:
                largeOnes[1] = nums[i]

        return largeIdx if largeOnes[1] is None or largeOnes[0] >= 2*largeOnes[1] else -1
