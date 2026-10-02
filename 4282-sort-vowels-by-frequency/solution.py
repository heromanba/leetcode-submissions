class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_idx = []
        vowel_cnt = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0,
        }
        first_occr = {
            'a': float('inf'),
            'e': float('inf'),
            'i': float('inf'),
            'o': float('inf'),
            'u': float('inf'),
        }
        char_arr = [c for c in s]
        for i in range(len(s)):
            if char_arr[i] in vowel_cnt:
                if vowel_cnt[char_arr[i]] == 0:
                    first_occr[char_arr[i]] = i
                vowel_cnt[char_arr[i]] += 1
                vowel_idx.append(i)
        i = 0
        for vowel, cnt in sorted(vowel_cnt.items(), key=lambda kv: (-kv[1], first_occr[kv[0]])):
            while cnt > 0:
                idx = vowel_idx[i]
                char_arr[idx] = vowel
                i += 1
                cnt -= 1
        return ''.join(char_arr)
