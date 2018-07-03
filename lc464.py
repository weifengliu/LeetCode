class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        maxSum = (1+maxChoosableInteger)*maxChoosableInteger/2
        self._d = {}

        return self.helper(list(range(1, maxChoosableInteger+1)), maxSum, desiredTotal)

    def helper(self, nums, maxSum, desiredTotal):
        if maxSum < desiredTotal or len(nums) == 0:
            return False

        hash = str(nums)
        if hash in self._d:
            return self._d[hash]

        if nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums)):
            if not self.helper(nums[:i]+nums[(i+1):], maxSum-nums[i], desiredTotal-nums[i]):
                self._d[hash] = True
                return True
        self._d[hash] = False
        return False
