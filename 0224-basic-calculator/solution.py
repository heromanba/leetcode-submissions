class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        operands = []
        operators = []
        i = 0
        while i < len(s):
            # print(i)
            # print(operators)
            # print(operands)
            if s[i].isdigit():
                token = []
                while i < len(s) and s[i].isdigit():
                    token.append(s[i])
                    i+=1
                if token:
                    operands.append(int(''.join(token)))
                continue
            elif s[i] == '-' and (
                i-1<0 or (i-1>=0 and s[i-1] == '(')
            ):
                operators.append('--')
            elif s[i] == '(':
                operators.append(s[i])
            elif s[i] in ('+', '-', ')'):
                while len(operators) > 0:
                    if operators[-1] == '(':
                        if s[i] == ')':
                            operators.pop()
                        break
                    operator = operators.pop()
                    if operator == '--':
                        operands[-1] = -operands[-1]
                    elif operator == '-':
                        rhs = operands.pop()
                        lhs = operands.pop()
                        operands.append(lhs-rhs)
                    elif operator == '+':
                        rhs = operands.pop()
                        lhs = operands.pop()
                        operands.append(lhs+rhs)
                operators.append(s[i])
            i += 1
    
        while operators:
            operator = operators.pop()
            if operator == '--':
                operands[-1] = -operands[-1]
            elif operator == '-':
                rhs = operands.pop()
                lhs = operands.pop()
                operands.append(lhs-rhs)
            elif operator == '+':
                rhs = operands.pop()
                lhs = operands.pop()
                operands.append(lhs+rhs)

        return operands[-1]
