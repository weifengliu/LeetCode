class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        currLen = 0
        prev = None
        for num in nums:
            if prev is None:
                prev = num
                currLen += 1
            else:
                if num <= prev:
                    prev = num
                    maxLen = max(maxLen, currLen)
                    currLen = 0
                prev = num
                currLen += 1
        maxLen = max(maxLen, currLen)
        return maxLen