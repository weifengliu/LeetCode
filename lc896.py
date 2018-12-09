class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True

        diff = None
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                continue
            if diff is None:
                diff = A[i] - A[i - 1]
            else:
                if diff * (A[i] - A[i - 1]) < 0:
                    return False

        return True
