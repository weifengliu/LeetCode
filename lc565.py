class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        self._visited = set()
        for i in range(len(nums)):
            if nums[i] not in self._visited:
                tmp = self._findS(i, nums)
                ret = max(ret, tmp)

        return ret

    def _findS(self, curr, nums):
        length = 0
        while curr not in self._visited:
            length += 1
            self._visited.add(curr)
            curr = nums[curr]

        return length
