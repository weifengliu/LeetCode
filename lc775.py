class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n==0:
            return True
        currMax = A[0]
        for i in range(n-2):
            currMax = max(currMax, A[i])
            if currMax > A[i+2]:
                return False

        return True