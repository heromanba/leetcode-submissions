# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        # base case, left child is not None
        if root.left:
            ptr = root.left
            while ptr.right:
                ptr = ptr.right
            ptr.right = root.right
            root.right = root.left
            root.left = None
        return
        
