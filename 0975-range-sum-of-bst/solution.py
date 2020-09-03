# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        range_sum = 0
        if L <= root.val <= R:
            range_sum += root.val
            
        if L < root.val:
            range_sum += self.rangeSumBST(root.left, L, R)
            
        if root.val < R:
            range_sum += self.rangeSumBST(root.right, L, R)
            
        return range_sum
