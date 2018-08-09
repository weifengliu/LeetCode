class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        self._cache = {}

        return self._dfs(0, len(A), A, K)

    def _dfs(self, start, end, A, K):
        key = (start, end, K)
        if key in self._cache:
            return self._cache[key]

        if K == 1:
            l = A[start:]
            self._cache[key] = sum(l)/float(len(l))
        else:
            curr = 0
            for j in range(start+1, end):
                l = A[start:j]
                curr = max(curr, sum(l)/float(len(l))+self._dfs(j, end, A, K-1))

            self._cache[key] = curr
        return self._cache[key]