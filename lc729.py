class Node:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start, end)
            return True
        else:
            curr = self.root
            while True:
                if end <= curr.s:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(start, end)
                        return True
                elif start >= curr.e:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(start, end)
                        return True
                else:
                    return False




        # Your MyCalendar object will be instantiated and called as such:
        # obj = MyCalendar()
        # param_1 = obj.book(start,end)