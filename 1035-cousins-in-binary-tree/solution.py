# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # bfs + queue
        if root is None:
            return False

        current_level = { root.val: (root, None) }
        while current_level:
            next_level = {}
            for node_val, (node, node_parent) in current_level.items():
                if node.left:
                    next_level.update({node.left.val: (node.left, node)})
                if node.right:
                    next_level.update({node.right.val: (node.right, node)})
                    
            if (x in next_level and y not in next_level) or \
                (x not in next_level and y in next_level):
                return False
            
            if x in next_level and y in next_level:
                if next_level[x][1] != next_level[y][1]:
                    return True
                else:
                    return False
                
            current_level = next_level
        return False
