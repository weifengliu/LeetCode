class RLEIterator:
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.start = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.start < len(self.A):
            if self.A[self.start] >= n:
                self.A[self.start] -= n
                return self.A[self.start + 1]
            else:
                n -= self.A[self.start]
                self.start += 2
        return -1



        # Your RLEIterator object will be instantiated and called as such:
        # obj = RLEIterator(A)
        # param_1 = obj.next(n)