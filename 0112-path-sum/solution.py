# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        # dfs + stack
        stack = [(root, 0)]
        while stack:
            node, path_sum = stack.pop()
            path_sum += node.val
            if not (node.left or node.right):
                if path_sum == sum:
                    return True
            if node.left:
                stack.append((node.left, path_sum))
            if node.right:
                stack.append((node.right, path_sum))
        return False
