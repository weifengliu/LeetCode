class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        currProduct = 1
        start = 0
        for end in range(len(nums)):
            currProduct *= nums[end]
            while currProduct >= k and start <= end:
                currProduct /= nums[start]
                start += 1
            count += (end-start+1)


        return count