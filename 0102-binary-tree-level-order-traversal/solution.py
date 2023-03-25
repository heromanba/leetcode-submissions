# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        frontier = [root]
        while frontier:
            result.append([n.val for n in frontier])
            next_level = []
            for node in frontier:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            frontier = next_level
        return result
