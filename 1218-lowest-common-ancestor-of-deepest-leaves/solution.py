# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        traversal = []
        heights = []
        def dfs(node, curr_h):
            if not node:
                return
            traversal.append(node)
            heights.append(curr_h)
            dfs(node.left, curr_h+1)
            if node.left:
                traversal.append(node)
                heights.append(curr_h)
            dfs(node.right, curr_h+1)
            if node.right:
                traversal.append(node)
                heights.append(curr_h)
        dfs(root, 0)
        max_h = max(heights)
        max_idx = set()
        for i in range(len(heights)):
            if heights[i] == max_h:
                max_idx.add(i)
        if len(max_idx) == 1:
            return traversal[list(max_idx)[0]]
        min_h, min_h_node = float('inf'), None
        for i in range(min(max_idx), max(max_idx)):
            h = heights[i]
            if h < min_h:
                min_h = h
                min_h_node = traversal[i]
        return min_h_node
        # print([node.val for node in max_h_nodes])
