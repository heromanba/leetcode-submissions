class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        cost = {
            ('01', '00'): 2,
            ('01', '10'): 3,
            ('01', '11'): 1,

            ('10', '00'): 2,
            ('10', '01'): 3,
            ('10', '11'): 1,

            ('00', '01'): 1,
            ('00', '10'): 1,
            ('00', '11'): 2,

            ('11', '00'): 1,
            ('11', '01'): 2,
            ('11', '10'): 2,

        }
        sl1 = [c for c in s1]
        sl2 = [c for c in s2]
        num_ops = 0
        for i in range(len(s1)):
            if i < len(s1)-2:
                if sl1[i] == sl2[i]:
                    continue
                elif sl1[i] == '0' and sl2[i] == '1':
                    num_ops += 1
                    continue
            if i < len(s1)-1 and sl1[i:i+2] != sl2[i:i+2]:
                transform = (sl1[i]+sl1[i+1], sl2[i]+sl2[i+1])
                num_ops += cost[transform]
                sl1[i] = sl2[i]
                sl1[i+1] = sl2[i+1]
            if i == len(s1)-1:
                if sl1[i]=='1' and sl2[i]=='0':
                    return -1
                elif sl1[i] == '0' and sl2[i] == '1':
                    num_ops += 1
        return num_ops


