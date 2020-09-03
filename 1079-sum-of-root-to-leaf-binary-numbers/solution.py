# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([(root, 0)])
        
        total_sum = 0
        
        # queue + bfs
        while queue:
            node, path_sum = queue.popleft()
            if node:
                # convert binary to decimal.
                path_sum = path_sum * 2 + node.val
                if not (node.left or node.right):
                    total_sum += path_sum
                queue.append((node.left, path_sum))
                queue.append((node.right, path_sum))
        return total_sum
