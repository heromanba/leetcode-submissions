class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if '+' not in expression \
            and '-' not in expression \
            and '*' not in expression:
            return [ int(expression) ]
        ret = []
        for i in range(len(expression)):
            if expression[i] in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if expression[i] == '+':
                            ret.append(l+r)
                        elif expression[i] == '-':
                            ret.append(l-r)
                        elif expression[i] == '*':
                            ret.append(l*r)
        return ret
                
