class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        tmp = ['' for _ in range(numRows)]
        for i in range(len(s)):
            mod = i%(2*numRows-2)
            if 0 <= mod < numRows:
                tmp[mod] += s[i]
            else:
                tmp[numRows-(mod-numRows)-2] += s[i]
        return ''.join(tmp)
