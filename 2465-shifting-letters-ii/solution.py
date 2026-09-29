import bisect
class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        ev_tmp = []
        for start, end, direction in shifts:
            if direction == 1:
                ev_tmp.append([start, 1])
                ev_tmp.append([end+1, -1])
            else:
                ev_tmp.append([start, -1])
                ev_tmp.append([end+1, 1])
        ev_tmp = sorted(ev_tmp, key=lambda x:x[0])
        ev = []
        for i in range(len(ev_tmp)):
            if i > 0 and ev_tmp[i][0] == ev[-1][0]:
                ev[-1][1] += ev_tmp[i][1]
            else:
                ev.append(ev_tmp[i])
        prefix = []
        for i in range(len(ev)):
            if i == 0:
                prefix.append(ev[0][1])
            else:
                prefix.append(prefix[i-1]+ev[i][1])
        ret = ''
        # print(ev)
        # print(prefix)
        # print('----------------------')
        for i in range(len(s)):
            idx = bisect.bisect_left(ev, i, key=lambda x:x[0])
            # print(i, idx)
            if idx >= len(ev) or (idx == 0 and ev[idx][0] != i):
                ret+=s[i]
            else:
                if ev[idx][0] != i:
                    offset = prefix[idx-1] 
                else:
                    offset = prefix[idx]
                # print(ev[idx][0], i, idx, 'offset: ', offset, chr((26+(ord(s[i])-ord('a')+offset)%26)%26+ord('a')))
                new_char = chr((26+(ord(s[i])-ord('a')+offset)%26)%26+ord('a'))
                ret += new_char
        return ret
