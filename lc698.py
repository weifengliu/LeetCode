class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        visited = [False]*len(nums)
        if k <= 0 or sum(nums)%k != 0:
            return False

        return self._dfs(nums, visited, 0, k, 0, sum(nums)/k)

    def _dfs(self, nums, visited, start, k, curr_sum, target):
        if k == 1:
            return True
        if curr_sum == target:
            return self._dfs(nums, visited, 0, k-1, 0, target)
        for i in range(start, len(nums)):
            if not visited[i]:
                visited[i] = True
                if self._dfs(nums, visited, i+1, k, curr_sum+nums[i], target):
                    return True
                visited[i] = False
        return False