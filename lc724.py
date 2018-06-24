class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left = -nums[-1]
        right = sum(nums)
        for i in range(0, len(nums)):
            left += nums[i-1]
            right -= nums[i]
            if left == right:
                return i

        return -1
