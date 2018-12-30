class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = [0] * 121
        scount = [0] * 121
        res = 0
        for age in ages:
            count[age] += 1
        for i in range(1, len(count)):
            scount[i] = scount[i - 1] + count[i]

        for age in range(15, 121):
            if count[age] == 0:
                continue
            res += (scount[age] - scount[int(age / 2) + 7]) * count[age] - count[age]

        return res