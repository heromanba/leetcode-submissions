# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lca(node, p, q):
            if node == p:
                return p
            if node == q:
                return q
            if not node:
                return
            left = lca(node.left, p, q)
            right = lca(node.right, p, q)
            if left and right:
                return node
            else:
                return left or right
        return lca(root, p, q)
