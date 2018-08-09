class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        swap = 1
        fixed = 0
        for i in range(1, n):
            if A[i] <= B[i-1] or B[i] <= A[i-1]:
                swap += 1
            elif A[i] <= A[i-1] or B[i] <= B[i-1]:
                tmp = swap
                swap = fixed+1
                fixed = tmp
            else:
                tmp = min(fixed, swap)
                fixed = tmp
                swap = tmp+1

        return min(swap, fixed)