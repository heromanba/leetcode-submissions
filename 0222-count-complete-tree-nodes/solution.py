# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        ret = 0
        while root:
            ret += 1
            root = root.left
        return ret

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        # print(root.val, lh, rh)
        if lh <= rh:
            return 2**lh-1 + self.countNodes(root.right) + 1
        else:
            return 2**rh-1 + self.countNodes(root.left) + 1
