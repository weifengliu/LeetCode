class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = [int(s) for s in list(str(num))]
        last = [None for _ in range(10)]
        for i in range(len(nums)):
            last[nums[i]] = i

        for i in range(len(nums)):
            for maxNum in range(9,-1,-1):
                if maxNum == nums[i]:
                    break
                if (last[maxNum] is not None) and last[maxNum] > i:
                    nums[i], nums[last[maxNum]] = maxNum, nums[i]
                    return int(''.join([str(x) for x in nums]))

        return num