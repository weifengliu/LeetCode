class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for i in range(len(S)):
            c = S[i]
            if c not in d:
                d[c] = []
            d[c].append(i)

        match = 0
        for word in words:
            positions = []
            currIdx = -1
            for c in word:
                if c not in d:
                    break
                for idx in d[c]:
                    if idx > currIdx:
                        positions.append(idx)
                        currIdx = idx
                        break

            if len(positions) == len(word):
                match += 1

        return match