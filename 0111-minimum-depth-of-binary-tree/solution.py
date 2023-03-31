# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # DFS
        if not root:
            return 0
        stack = [(root, 1)]
        minLen = float('inf')
        while stack:
            curr, pathLen = stack.pop()
            if curr.right:
                stack.append((curr.right, pathLen + 1))
            if curr.left:
                stack.append((curr.left, pathLen + 1))
            # leaf node
            if (not curr.left) and (not curr.right):
                if pathLen < minLen:
                    minLen = pathLen
        return minLen


            
