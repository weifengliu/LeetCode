class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        char_counts = [0]*26
        for task in tasks:
            char_counts[ord(task)-ord('A')] += 1
        char_counts.sort()

        i = 25
        while i>=0 and char_counts[i]==char_counts[25]:
            i -= 1

        return max(len(tasks), (char_counts[25]-1)*(n+1)+(25-i))
