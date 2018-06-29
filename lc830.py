class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        n = len(S)
        ret = []

        if n<=1:
            return ret

        start = 0
        prev = S[0]
        for i in range(1, n):
            if S[i] != prev:
                if i-start >= 3:
                    ret.append([start, i-1])
                prev = S[i]
                start = i

        if i-start >= 2:
            ret.append([start, i])

        return ret