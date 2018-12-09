class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {list1[i]: i for i in range(len(list1))}
        ret = []
        minSum = len(list1) + len(list2)

        for j in range(len(list2)):
            if list2[j] in d:
                currSum = j + d[list2[j]]
                if currSum < minSum:
                    minSum = currSum
                    ret = [list2[j]]
                elif currSum == minSum:
                    ret.append(list2[j])
        
        return ret