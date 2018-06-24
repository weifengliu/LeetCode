class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        idx = 0
        n = len(bits)
        while idx < n-1:
            if bits[idx] == 0:
                idx += 1
            else:
                idx += 2

        return idx < n