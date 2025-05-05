class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        dp = [
            [
                1 if i >= j else None
                for j in range(len(s))
            ]
            for i in range(len(s))
        ]
        max_len = 1
        ret = s[0]
        for offset in range(1, len(s)):
            for i in range(0, len(s)-offset):
                j = i + offset
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 0
                if dp[i][j] == 1 and j-i+1 > max_len:
                    max_len = j-i+1
                    ret = s[i:j+1]
        return ret


