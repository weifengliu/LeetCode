class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_so_far = A[0]
        disjoint = 0
        peak = A[disjoint]
        for i in range(len(A)):
            max_so_far = max(max_so_far, A[i])
            if A[i] < peak:
                disjoint = i
                peak = max_so_far

        return disjoint + 1