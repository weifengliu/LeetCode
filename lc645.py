class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        n = len(nums)
        d = {x: 0 for x in range(1, n+1)}
        for num in nums:
            d[num] += 1
            if d[num] > 1:
                ret.append(num)

        for k in d.keys():
            if d[k] == 0:
                ret.append(k)
                return ret