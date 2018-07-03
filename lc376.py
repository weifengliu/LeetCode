class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return 0

        up = [0]*n
        down = [0]*n
        up[0] = 1
        down[0] = 1

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                up[i] = up[i-1]
                down[i] = up[i-1] + 1
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]

        return max(up[-1], down[-1])