# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        stack = []
        traversal = [TreeNode(float('-inf'))]
        current = root
        while stack or current:
            while current:  # Traverse to leftmost node
                stack.append(current)
                current = current.left
            current = stack.pop()
            traversal.append(current)
            current = current.right  # Move to right subtree
        traversal.append(TreeNode(float('inf')))
        # find two nodes that are not in ascending order
        first, second = None, None
        for i in range(1, len(traversal)-1):
            if not first and traversal[i-1].val < traversal[i].val > traversal[i+1].val:
                first = traversal[i]
            if traversal[i-1].val > traversal[i].val < traversal[i+1].val:
                second = traversal[i]
        first.val, second.val = second.val, first.val
        
        
