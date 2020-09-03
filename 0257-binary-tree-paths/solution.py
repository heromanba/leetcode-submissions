# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return root
        queue = collections.deque([(root, "")])
        path_list = []
        while queue:
            node, path = queue.popleft()
            if not (node.left or node.right):
                path_list.append(path+f"{node.val}")
            if node.left:
                queue.append((node.left, path+f"{node.val}->"))
            if node.right:
                queue.append((node.right, path+f"{node.val}->"))
        return path_list
    
