from collections import deque
class FrontMiddleBackQueue:

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.rebalance()
        # print('pushFront', val, self.left, self.right)

    def pushMiddle(self, val: int) -> None:
        self.right.appendleft(val)
        self.rebalance()        
        # print('pushMiddle', val, self.left, self.right)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.rebalance()   
        # print('pushBack', val, self.left, self.right)
        

    def popFront(self) -> int:
        # print('popFront', self.left, self.right)
        val = -1
        if self.left:
            val = self.left.popleft()
        elif self.right:
            val = self.right.popleft()
        self.rebalance()
        return val

    def popMiddle(self) -> int:
        # print('popMiddle', self.left, self.right)
        if not self.right:
            return -1
        if len(self.left) == len(self.right):
            val = self.left.pop()
        else:
            val = self.right.popleft()
        self.rebalance()
        return val
        

    def popBack(self) -> int:
        # print('popBack', self.left, self.right)
        if not self.right:
            return -1
        val = self.right.pop()
        self.rebalance()
        return val
        
    def rebalance(self) -> None:
        # 1 >= keep len(r) - len(l) >= 0
        if len(self.right) - len(self.left) > 1:
            self.left.append(self.right.popleft())
        if len(self.right) - len(self.left) < 0:
            self.right.appendleft(self.left.pop())


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
