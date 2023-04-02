# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = [ root ]
        visited = set()
        sum_val = 0
        while stack:
            curr_node = stack.pop()
            if curr_node.left:
                if not stack or (curr_node.left is not stack[-1]):
                    stack.append(curr_node.left)
            stack.append(curr_node)
            if curr_node.right and (curr_node.right not in visited):
                stack.append(curr_node.right)
            if not curr_node.right or (curr_node.right in visited):
                sum_val += curr_node.val
                curr_node.val = sum_val
                stack.pop()
                visited.add(curr_node)
        return root 

