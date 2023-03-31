# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        frontier = [ root ]
        last_level = []
        while frontier:
            next_level = []
            for n in frontier:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            if not next_level:
                last_level = frontier
            frontier = next_level
        return sum([n.val for n in last_level])
