# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # bfs + queue
        if root is None:
            return 0
        current_level = [root]
        left_leaf_sum = 0
        while current_level:
            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                    # check if left child is leaf.
                    if not (node.left.left or node.left.right):
                        left_leaf_sum += node.left.val
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
        return left_leaf_sum
