class Solution:
    def minFlips(self, s: str) -> int:
        num_ones = 0
        first_one_idx = None
        last_one_idx = None
        for i in range(len(s)):
            if s[i] == '1':
                if first_one_idx is None:
                    first_one_idx = i
                last_one_idx = i
                num_ones += 1
        if num_ones <= 1:
            return 0
        else:
            ones_to_keep = 1
            if first_one_idx == 0 and last_one_idx == len(s)-1:
                ones_to_keep = 2
            return min(num_ones-ones_to_keep, len(s)-num_ones)

