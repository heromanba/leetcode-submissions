class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        ops_priority = {
            '+': 0,
            '-': 0,
            '*': 1,
            '/': 1,
        }
        operands = []
        operators = []
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] in ops_priority:
                while len(operators) > 0 and ops_priority[s[i]] <= ops_priority[operators[-1]]:
                    operator = operators.pop()
                    right_operand = operands.pop()
                    left_operand = operands.pop()
                    operands.append(self._apply_operator(left_operand, operator, right_operand))
                operators.append(s[i])
                i += 1
            else:
                token_list = []
                # print(i, s[i])
                while i < len(s) and s[i].isdigit():
                    token_list.append(s[i])
                    i += 1
                operands.append(int(''.join(token_list)))
    
        while len(operators) > 0:
            operator = operators.pop()
            right_operand = operands.pop()
            left_operand = operands.pop()
            operands.append(self._apply_operator(left_operand, operator, right_operand))
        return operands[-1]

    def _apply_operator(self, left_operand, operator, right_operand):
        if operator == '+':
            return left_operand+right_operand
        elif operator == '-':
            return left_operand-right_operand
        elif operator == '*':
            return left_operand*right_operand
        elif operator == '/':
            return int(left_operand/right_operand)

