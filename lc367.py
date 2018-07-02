class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        n = len(p)
        if n <= 1:
            return n

        d = {p[0]:1}
        prev = 1

        for i in range(1, n):
            if p[i] not in d:
                d[p[i]] = 1
            if (p[i] == 'a' and p[i-1] == 'z') or (ord(p[i]) - ord(p[i-1]) == 1):
                curr = prev+1
                d[p[i]] = max(d[p[i]], curr)
            else:
                curr = 1
            prev = curr

        return sum(d.values())

s1 = Solution()
print(s1.findSubstringInWraproundString("aabb"))
