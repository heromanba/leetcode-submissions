class Solution:
    def replaceDigits(self, s: str) -> str:
        ret = ""
        for i in range(len(s)//2):
            ret += s[2*i] + chr(ord(s[2*i]) + int(s[2*i+1]))
        if len(s) %  2 != 0:
            ret += s[-1]
        return ret
