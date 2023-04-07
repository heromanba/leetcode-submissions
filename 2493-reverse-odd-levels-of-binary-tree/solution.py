# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr_level = [ root ]
        level = 0
        while curr_level:
            next_level = []
            for i, node in enumerate(curr_level):
                if (level % 2 == 1) and (i < len(curr_level)//2):
                    node.val, curr_level[-i-1].val = curr_level[-i-1].val, node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr_level = next_level
            level += 1
        return root
