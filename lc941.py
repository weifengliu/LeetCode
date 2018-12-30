class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 1:
            return False

        if A[1] <= A[0]:
            return False
        isUp = True
        prev = A[0]
        for curr in A[1:]:
            if isUp:
                if curr > prev:
                    prev = curr
                elif curr == prev:
                    return False
                else:
                    isUp = False
                    prev = curr
            else:
                if curr < prev:
                    prev = curr
                    continue
                else:
                    return False

        return not isUp