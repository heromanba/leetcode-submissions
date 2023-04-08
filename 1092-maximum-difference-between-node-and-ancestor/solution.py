# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = float('-inf')
        def minMax(node):
            if (not node.left) and (not node.right):
                return node.val, node.val
            l_min, l_max = float('inf'), float('-inf')
            if node.left:
                l_min, l_max = minMax(node.left)
            r_min, r_max = float('inf'), float('-inf')
            if node.right:
                r_min, r_max = minMax(node.right)
            min_v = min(node.val, l_min, r_min)
            max_v = max(node.val, l_max, r_max)
            nonlocal max_diff
            if abs(max_v - node.val) > max_diff:
                max_diff = abs(max_v - node.val)
            if abs(min_v - node.val) > max_diff:
                max_diff = abs(min_v - node.val)
            return min_v, max_v 
        minMax(root)
        return max_diff
