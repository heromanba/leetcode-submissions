# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return root
        stack = [root]
        val_set = {root.val}
        while stack:
            node = stack.pop()
            if node:
                if node.val not in val_set:
                    return False
                stack.append(node.left)
                stack.append(node.right)
        return True
