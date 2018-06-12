class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=0:
            return 0

        n = len(nums)
        curr_max, curr_min = nums[0], nums[n-1]
        left = n-1
        right = 0


        for i in range(len(nums)):
            curr_max = max(curr_max, nums[i])
            curr_min = min(curr_min, nums[n-1-i])
            if nums[i]<curr_max:
                right = i
            if nums[n-1-i]>curr_min:
                left = n-1-i


        return right-left+1 if right>left else 0


