class Solution:
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        if N == 0:
            return 0.5
        if N >= 5000:
            return 1.0

        self._cache = {}
        return self._dfs(N, N)

    def _dfs(self, A, B):
        key = (A, B)
        if key in self._cache:
            return self._cache[key]

        if A <= 0 and B <= 0:
            return 0.5
        elif A <= 0:
            return 1
        elif B <= 0:
            return 0
        else:
            self._cache[key] = 0.25 * (self._dfs(A - 100, B)
                                       + self._dfs(A - 75, B - 25)
                                       + self._dfs(A - 50, B - 50)
                                       + self._dfs(A - 25, B - 75))
        return self._cache[key]