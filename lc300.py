class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        longest = [1]*n
        ret = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    longest[i] = max(longest[i], longest[j]+1)
            ret = max(ret, longest[i])
        
        return ret