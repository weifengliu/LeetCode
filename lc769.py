class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        currBoundry = 0
        chunk = 0
        for i in range(len(arr)):
            if i<=currBoundry:
                currBoundry = max(currBoundry, arr[i])
            else:
                chunk += 1
                currBoundry = arr[i]
        chunk += 1

        return chunk