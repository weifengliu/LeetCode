class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        currSum = 0
        remain = {0:-1}

        for i in range(len(nums)):
            currSum += nums[i]
            r = currSum % k if k != 0 else currSum
            if r not in remain:
                if r == 0 and i >= 1:
                    return True
                remain[r] = i
            else:
                if i - remain[r] > 1:
                    return True

        return False

s1 = Solution()
s1.checkSubarraySum([0,1,0], 0)