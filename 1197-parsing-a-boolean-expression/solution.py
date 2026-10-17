class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        s= expression
        stack = []
        for i in range(len(expression)):
            if s[i] == ',':
                continue
            elif s[i] != ')':
                c = s[i]
                if c == 't':
                    c = True
                if c == 'f':
                    c = False                
                stack.append(c)
            else:
                tmp_stack = []
                top = stack.pop()
                while top != '(':
                    tmp_stack.append(top)
                    top = stack.pop()
                op = stack.pop()
                if op == '|':
                    stack.append(any(tmp_stack))
                elif op == '&':
                    stack.append(all(tmp_stack))
                elif op == '!':
                    stack.append(not tmp_stack[0])
        return stack[-1]

