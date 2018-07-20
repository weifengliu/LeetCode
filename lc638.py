class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self._cache = {}
        self._options = special

        return self._helper(tuple(needs), price)

    def _helper(self, t_needs, price):
        if t_needs in self._cache:
            return self._cache[t_needs]

        self._cache[t_needs] = sum([price[i]*t_needs[i] for i in range(len(price))])
        for option in self._options:
            remain = [t_needs[i] - option[i] for i in range(len(t_needs))]
            valid = True
            for x in remain:
                if x<0:
                    valid = False
                    break

            if valid:
                self._cache[t_needs] = min(self._cache[t_needs], option[-1]+self._helper(tuple(remain), price))

        return self._cache[t_needs]