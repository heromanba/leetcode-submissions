class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        base = 5
        modulus = pow(10, 9) + 7
        char_set = {
            'A': 0,
            'C': 1,
            'G': 2,
            'T': 3,
        }
        seq_cnt = {}
        hash_to_seq = {}
        rolling = 0
        pow1 = pow(base, 9)
        for i in range(len(s)-10+1):
            # print(i, i+9, len(s))
            if i == 0:
                for j in range(10):
                    rolling = (rolling * base + char_set[s[j]])%modulus
            else:
                rolling = (rolling - char_set[s[i-1]] * pow1)%modulus
                rolling = (rolling * base + char_set[s[i+9]])%modulus
            # if s[i:i+10] == 'TTTTTTGTTT':
            #     print(rolling in seq_cnt)
            if rolling in seq_cnt:
                seq_cnt[rolling] += 1
                hash_to_seq[rolling] = s[i:i+10]
            else:
                seq_cnt[rolling] = 1
        ret = []
        for rolling, cnt in seq_cnt.items():
            if cnt > 1:
                ret.append(hash_to_seq[rolling])
        return ret
