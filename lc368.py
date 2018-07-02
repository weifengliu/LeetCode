class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        nums = sorted(nums)
        d = {num:[num] for num in nums}
        ret = []

        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    if len(d[nums[i]]) <= len(d[nums[j]]):
                        d[nums[i]] = list(d[nums[j]])
                        d[nums[i]].append(nums[i])

            ret = d[nums[i]] if len(d[nums[i]]) > len(ret) else ret
        return ret