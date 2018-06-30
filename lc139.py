class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        couldBreak = [False]*(n+1)
        couldBreak[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if couldBreak[j] and s[j:i] in wordDict:
                    couldBreak[i] = True
                    break

        return couldBreak[-1]