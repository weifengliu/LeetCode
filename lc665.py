class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 1:
            return True
        count = 0
        prev = nums[0]
        for i in range(1, n):
            if nums[i] < prev:
                if count > 0:
                    return False
                count += 1
                if i-2 < 0 or nums[i] >= nums[i-2]:
                    prev = nums[i]
            else:
                prev = nums[i]
        return True