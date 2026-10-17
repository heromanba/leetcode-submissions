from collections import deque

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ')':
                stack.append(s[i])
            else:
                reverse = deque()
                top = stack.pop()
                while top != '(':
                    reverse.append(top)
                    top = stack.pop()
                while len(reverse) > 0:
                    stack.append(reverse.popleft())
            i += 1
        return ''.join(stack)

