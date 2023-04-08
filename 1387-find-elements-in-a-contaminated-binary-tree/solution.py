# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        level = 1
        mapping = dict()
        curr_level = [root]
        while curr_level:
            mapping[level] = curr_level
            next_level = []
            for node in curr_level:
                if node.left:
                    node.left.val = 2 * node.val + 1
                    next_level.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    next_level.append(node.right)
            curr_level = next_level
            level += 1
        self.mapping = mapping
            

    def find(self, target: int) -> bool:
        n = math.ceil(math.log(target+2, 2))
        if n in self.mapping:
            for node in self.mapping[n]:
                if node.val == target:
                    return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
