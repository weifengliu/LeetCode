class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        prev = None
        maxDistance = 0
        for i in range(len(seats)):
            if seats[i]:
                if prev is None:
                    maxDistance = max(maxDistance, i)
                else:
                    if (i-prev)%2:
                        maxDistance = max(maxDistance, (i-prev-1)/2)
                    else:
                        maxDistance = max(maxDistance, (i-prev)/2)
                prev = i

        if prev != i:
            maxDistance = max(maxDistance, i-prev)

        return maxDistance