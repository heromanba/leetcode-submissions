# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def getGrandchildrenSum(node):
            sum_v = 0
            if node.left:
                if node.left.left:
                    sum_v += node.left.left.val
                if node.left.right:
                    sum_v += node.left.right.val
            if node.right:
                if node.right.left:
                    sum_v += node.right.left.val
                if node.right.right:
                    sum_v += node.right.right.val
            return sum_v
        sum_v_total = 0
        def preOrder(node):
            if not node:
                return
            if node.val % 2 == 0:
                nonlocal sum_v_total
                sum_v_total += getGrandchildrenSum(node)
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)
        return sum_v_total
