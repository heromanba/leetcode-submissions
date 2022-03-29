# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # base case
        if root is None:
            return True
        if (not root.left) and (not root.right):
            root.minVal = root.val
            root.maxVal = root.val
            return True
        elif root.left and (not root.right):
            if self.isValidBST(root.left) and (root.val > root.left.maxVal):
                root.minVal = min(root.val, root.left.minVal)
                root.maxVal = max(root.val, root.left.maxVal)
                return True
            else:
                return False
        elif (not root.left) and root.right:
            if self.isValidBST(root.right) and (root.val < root.right.minVal):
                root.minVal = min(root.val, root.right.minVal)
                root.maxVal = max(root.val, root.right.maxVal)
                return True
            else:
                return False
        elif root.left and root.right:
            if self.isValidBST(root.left) and self.isValidBST(root.right) and (root.val > root.left.maxVal) and (root.val < root.right.minVal):
                root.minVal = min(root.val, root.left.minVal, root.right.minVal)
                root.maxVal = max(root.val, root.left.maxVal, root.right.maxVal)
                return True
            else: 
                return False
