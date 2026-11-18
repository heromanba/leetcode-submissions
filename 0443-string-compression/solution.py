class Solution:
    def compress(self, chars: list[str]) -> int:
        cs = []
        cnt = []
        for c in chars:
            if cs and c == cs[-1]:
                cnt[-1] += 1
                continue
            else:
                cs.append(c)
                cnt.append(1)
        result = []
        for i in range(len(cs)):
            result.append(cs[i])
            if cnt[i] > 1:
                result.extend([c for c in str(cnt[i])])
        # print(result)
        chars[:len(result)] = result
        return len(result)
