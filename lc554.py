class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = {}
        count = 0
        for row in wall:
            length = 0
            for brick in row[:-1]:
                length += brick
                if length not in d:
                    d[length] = 0
                d[length] += 1
                count = max(count, d[length])

        return len(wall)-count