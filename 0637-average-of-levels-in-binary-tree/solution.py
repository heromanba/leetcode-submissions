# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # lever order traversal
        if root is None:
            return []
        current_level = [root]
        result = []
        while current_level:
            next_level = []
            current_level_sum = 0
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                current_level_sum += node.val
            result.append(current_level_sum / len(current_level))
            current_level = next_level
        return result
