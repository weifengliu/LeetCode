class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for char in t:
            if char not in d:
                d[char] = 0
            d[char] += 1

        start = 0
        end = 0
        count = len(t)
        ret = None

        for end in range(len(s)):
            if s[end] not in d:
                continue
            d[s[end]] -= 1
            if d[s[end]] >= 0:
                count -= 1
            while count == 0:
                if ret is None or end - start + 1 < len(ret):
                    ret = s[start:(end + 1)]
                if s[start] in d:
                    d[s[start]] += 1
                    if d[s[start]] > 0:
                        count += 1
                start += 1
                while start < end and s[start] not in d:
                    start += 1

        return ret if ret is not None else ""
