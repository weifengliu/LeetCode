class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        new_A = sorted(A)
        new_B = sorted(B)
        diff = (sum(A) - sum(B)) / 2
        i, j = 0, 0
        while i < len(new_A):
            while j < len(new_B) and new_A[i] - new_B[j] > diff:
                j += 1
            if new_A[i] - new_B[j] == diff:
                return [new_A[i], new_B[j]]

            i += 1