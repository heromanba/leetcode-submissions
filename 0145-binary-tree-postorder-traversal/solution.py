# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return root
        
        stack = [(root, False)]
        traversal = []
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # whether children have been visited.
                    traversal.append(node.val)
                else:
                    stack.append((node, True))    # key point.
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return traversal
        
