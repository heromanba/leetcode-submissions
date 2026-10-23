# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        priority = { '+':1,'-':1,'*':2,'/':2 }
        
        operands = []
        operators = []
        
        def eval_op():
            op = operators.pop()
            rhs = operands.pop()
            lhs = operands.pop()
            # print(op.val, rhs.val, lhs.val)
            node = Node(val=op.val, left=lhs, right=rhs)
            operands.append(node)

        expr_nodes = [Node(val) for val in s]
        # print(expr_nodes)
        for node in expr_nodes:
            if node.val.isdigit():
                operands.append(node)
            elif node.val == '(':
                operators.append(node)
            elif node.val in priority:
                while len(operators) > 0 and \
                    operators[-1].val in priority and \
                    priority[node.val] <= priority[operators[-1].val]:
                    eval_op()
                operators.append(node)
            elif node.val == ')':
                while operators[-1].val != '(':
                    eval_op()
                operators.pop()

        while len(operators) > 0:
            eval_op()
        # print(operands[0].val)
        return operands[0]
