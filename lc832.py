class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [ list(x) for x in A ]

        for row in ret:
            i = 0
            j = len(row)-1
            while i<=j:
                if row[i] == row[j]:
                    row[i] = row[j] = int(not row[i])
                i += 1
                j -= 1

        return ret