# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        stack = []
        node = root
        
        greater_sum = 0
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.right    # reversed inorder
            node = stack.pop()
            node.val += greater_sum
            greater_sum = node.val
            node = node.left
        return root
