# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # inorder traversal
        if root is None:
            return 0
        node = root
        stack = []
        
        # key point: use inf.
        min_diff, prev_val = float('inf'), float('inf')
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            
            diff = abs(node.val - prev_val)
            if diff < min_diff:
                min_diff = diff
            prev_val = node.val
            node = node.right
        return min_diff
