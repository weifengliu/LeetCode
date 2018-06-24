class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = len(nums)
        count = {}
        last = {}
        first = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in count:
                count[num] = 0
            if num not in last:
                last[num] = i
            if num not in first:
                first[num] = i
            count[num] += 1
            last[num] = i
        
        maxFreq = max(count.values())
        for candidate in count:
            if count[candidate] == maxFreq:
                ret = min(ret, last[candidate]-first[candidate]+1)
        
        return ret
        