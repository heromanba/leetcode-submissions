# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        traversal = []
        heights = []
        def dfs(node, curr_h):
            if not node:
                return
            traversal.append(node)
            heights.append(curr_h)
            
            if node.left:
                dfs(node.left, curr_h+1)
                
                traversal.append(node)
                heights.append(curr_h)

            if node.right:    
                dfs(node.right, curr_h+1)
            
        dfs(root, 0)
        
        p_idx = traversal.index(p)
        q_idx = traversal.index(q)

        min_h = float('inf')
        min_h_node = None
        for i in range(min(p_idx, q_idx), max(p_idx, q_idx)):
            if heights[i] < min_h:
                min_h = heights[i]
                min_h_node = traversal[i]
                
        return min_h_node

