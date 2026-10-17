class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        i = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                score = 0
                top = stack.pop()
                while top != '(':
                    score += top
                    top = stack.pop()
                if score == 0:
                    score = 1
                else:
                    score = score * 2
                stack.append(score)
            
        return sum(stack)
