# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        stack = [(root, root.val)]
        parent = { root: None }
        while stack:
            curr_node, curr_sum = stack.pop()
            if curr_node.right:
                stack.append((curr_node.right, curr_sum + curr_node.right.val))
                parent[curr_node.right] = curr_node
            if curr_node.left:
                stack.append((curr_node.left, curr_sum + curr_node.left.val))
                parent[curr_node.left] = curr_node
            if (not curr_node.left) and (not curr_node.right):
                if curr_sum == targetSum:
                    path = []
                    while True:
                        if curr_node is not None:
                            path.append(curr_node.val)
                            curr_node = parent[curr_node]
                        else:
                            break
                    result.append(reversed(path))
        return result
