class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxSum = sum(nums[0:k])
        currSum = maxSum
        for i in range(k, len(nums)):
            currSum = currSum+nums[i]-nums[i-k]
            maxSum = max(maxSum, currSum)

        return maxSum/k