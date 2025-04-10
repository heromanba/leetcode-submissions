class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        direction = 1
        if not s:
            return 0
        if s[0] == "-":
            s = s[1:]
            direction = -1
        elif s[0] == "+":
            s = s[1:]
        s = s.lstrip('0')
        i = 0
        while i < len(s):
            if s[i] not in "0123456789":
                break
            i += 1
        ret = int(s[:i] or 0) * direction
        if ret > 2**31-1:
            return 2**31-1
        elif ret < -2**31:
            return -2**31
        else:
            return ret
