# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened = []
        def dfs(nested_int):
            if nested_int.isInteger():
                self.flattened.append(nested_int.getInteger())
                return
            for ni in nested_int.getList():
                dfs(ni)
        for ni in nestedList:
            dfs(ni)
        self.iterator = iter(self.flattened)
        self.has_next = len(self.flattened) > 0
        self.next_val = next(self.iterator) if self.has_next else None
        # print(self.flattened, self.has_next)
        # print(self.flattened)
    
    def next(self) -> int:
        val = self.next_val
        try:
            self.next_val = next(self.iterator)
        except StopIteration:
            self.has_next = False
        return val
    
    def hasNext(self) -> bool:
        return self.has_next

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
