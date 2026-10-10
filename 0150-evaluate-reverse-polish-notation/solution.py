class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {'+','-','*','/'}:
                stack.append(int(t))
                continue
            op2 = int(stack.pop())
            op1 = int(stack.pop())
            if t == '+':
                stack.append(op1+op2)
            elif t == '-':
                stack.append(op1-op2)
            elif t == '*':
                stack.append(op1*op2)
            elif t == '/':
                stack.append(int(op1/op2))
            # print(t, op1, op2, stack)
        return stack[-1]
