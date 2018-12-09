class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        maxLen = 0
        for k in sorted(d.keys()):
            if k+1 in d:
                maxLen = max(maxLen, d[k]+d[k+1])

        return maxLen