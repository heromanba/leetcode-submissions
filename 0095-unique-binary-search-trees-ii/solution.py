# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        values = [ i for i in range(1, n+1) ]
        def generate(num_nodes, vals):
            if num_nodes == 0:
                return [ None ]
            ret = []
            for i in range(1, num_nodes+1):
                left_subtrees = generate(i-1, vals[:i-1])
                right_subtrees = generate(num_nodes-i, vals[i:])
                for l_tree in left_subtrees:
                    for r_tree in right_subtrees:
                        root = TreeNode(vals[i-1])
                        root.left = l_tree
                        root.right = r_tree
                        ret.append(root)
            return ret
        return generate(n, values)


