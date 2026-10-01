class Solution:
    def longestPrefix(self, s: str) -> str:
        ans = ""

        base1 = 29
        modulus1 = pow(10, 9) + 7
        
        base2 = 31
        modulus2 = pow(10, 9) + 3 

        prefix_rolling1 = 0
        prefix_rolling2 = 0

        suffix_rolling1 = 0
        suffix_rolling2 = 0
        power1 = 1
        power2 = 1
        for i in range(len(s)-1):
            prefix_rolling1 = (prefix_rolling1 * base1 + (ord(s[i])-ord('a'))) % modulus1
            prefix_rolling2 = (prefix_rolling2 * base2 + (ord(s[i])-ord('a'))) % modulus2

            suffix_rolling1 = ((ord(s[-i-1])-ord('a')) * power1 + suffix_rolling1) % modulus1
            suffix_rolling2 = ((ord(s[-i-1])-ord('a')) * power2 + suffix_rolling2) % modulus2

            power1 = (power1*base1)%modulus1
            power2 = (power2*base2)%modulus2

            if (prefix_rolling1, prefix_rolling2) == (suffix_rolling1, suffix_rolling2):
                ans = s[:i+1]
        return ans
