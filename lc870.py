class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sortA = sorted(A)
        d = collections.defaultdict(list)
        for b in sorted(B)[::-1]:
            if b < sortA[-1]:
                d[b].append(sortA.pop())

        return [(d[b] or sortA).pop() for b in B]