class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        use = 0
        nouse = 0
        prev = -1
        for num in sorted(d.keys()):
            curr = use
            if num - prev > 1:
                use = max(use, nouse) + num * d[num]
                nouse = max(curr, nouse)
            else:
                use = nouse + num * d[num]
                nouse = max(curr, nouse)
            prev = num

        return max(use, nouse)