class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        start = 0
        count = 0

        for i in range(len(A)):
            if L <= A[i] <= R:
                count = i - start + 1
                res += count
            elif A[i] < L:
                res += count
            else:
                start = i+1
                count = 0

        return res