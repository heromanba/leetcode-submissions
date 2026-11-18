from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        stack = deque()
        for idx, n in enumerate(num):
            while stack and stack[-1] > n and len(num)-k-(len(stack)-1) <= len(num)-idx:
                stack.pop()
            if len(stack) < len(num)-k:
                stack.append(n)
        while len(stack)>1 and stack[0] == '0':
            stack.popleft()
        return ''.join(stack)
            

