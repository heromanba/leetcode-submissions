# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        frontier = [root]
        while frontier:
            result.append([node.val for node in frontier])
            next_level = []
            for node in frontier:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            frontier = next_level
            next_level = []
        return reversed(result)

