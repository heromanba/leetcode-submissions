# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllLeaf(self, root):
        # run postorder traversal
        if root is None:
            return root
        stack = [root]
        allLeaf = []
        while stack:
            node = stack.pop()
            if node:
                if not (node.left or node.right):
                    allLeaf.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return allLeaf
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        allLeaf1 = self.getAllLeaf(root1)
        allLeaf2 = self.getAllLeaf(root2)
        print(allLeaf1)
        print(allLeaf2)
        return allLeaf1 == allLeaf2
            
