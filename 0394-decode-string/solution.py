class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            # print(stack)
            if s[i].isdigit():
                nums = []
                while i < len(s) and s[i].isdigit():
                    nums.append(s[i])
                    i+=1
                stack.append(int(''.join(nums)))
            elif s[i].isalpha():
                letters = []
                while i < len(s) and s[i].isalpha():
                    letters.append(s[i])
                    i+=1
                stack.append(''.join(letters))
            elif s[i] == '[':
                stack.append(s[i])
                i += 1
            elif s[i] == ']':
                string = stack.pop()
                while len(stack) > 0 and stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop() # left bracket
                num = stack.pop()
                stack.append(string*num)
                i+=1
        return ''.join(stack)
