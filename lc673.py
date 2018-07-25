class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        maxLen = 1
        dp = [1] * len(nums)
        count = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    curr = 1 + dp[j]
                    if curr > dp[i]:
                        dp[i] = curr
                        count[i] = count[j]
                    elif dp[j]+1 == dp[i]:
                        count[i] += count[j]

            maxLen = max(maxLen, dp[i])

        for i in range(len(nums)):
            if dp[i] == maxLen:
                ret += count[i]

        return ret