class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ret = [None]*n
        i = 1
        j = n
        for idx in range(n):
            if k==1:
                ret[idx] = i
                i += 1
            else:
                if k%2:
                    ret[idx] = i
                    i += 1
                else:
                    ret[idx] = j
                    j -= 1
                k -= 1

        return ret