class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = (max_len - len(a)) * '0' + a
        b = (max_len - len(b)) * '0' + b
        s = ""
        add = 0
        for i in range(1, max_len+1):
            a_i = int(a[-i])
            b_i = int(b[-i])
            s_i = a_i + b_i + add
            print(a_i, b_i)
            if s_i > 1:
                s = str(s_i % 2) + s
                add = 1
            else:
                s = str(s_i) + s
                add = 0
        if add:
            s = str(add) + s
        return s
