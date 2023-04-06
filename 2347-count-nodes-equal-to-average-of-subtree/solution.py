# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ret = []
        # modified recursive postorder
        def stats(node, sum_v, num):
            if not node:
                return 0, 0
            l_sum, l_num = stats(node.left, sum_v, num)
            r_sum, r_num = stats(node.right, sum_v, num)
            sum_v, num = l_sum + r_sum + node.val, l_num + r_num + 1
            if sum_v // num == node.val:
                ret.append(node.val)
            return sum_v, num
        stats(root, 0, 0)
        return len(ret)
        


