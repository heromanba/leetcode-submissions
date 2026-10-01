class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ans = ""
        low = 1
        high = len(s)+1
        while low < high:
            mid = low + (high-low)//2
            dup = self.check_dup(s, mid)
            if dup:
                ans = dup
                low = mid + 1
            else:
                high = mid
        return ans
    
    def check_dup(self, s, target_len):
        base1 = 29
        modulus1 = pow(10, 9) + 7
        power1 = pow(base1, target_len-1, modulus1)

        base2 = 31
        modulus2 = pow(10, 9) + 3
        power2 = pow(base2, target_len-1, modulus2)

        hashset = set()

        rolling1 = 0
        rolling2 = 0
        for i in range(len(s)-target_len+1):
            if i == 0:
                for j in range(target_len):
                    rolling1 = (rolling1 * base1 + ord(s[j])-ord('a')) % modulus1
                    rolling2 = (rolling2 * base2 + ord(s[j])-ord('a')) % modulus2
            else:
                rolling1 = (rolling1 - (ord(s[i-1])-ord('a'))*power1) % modulus1
                rolling1 = (rolling1*base1 + ord(s[i+target_len-1])-ord('a')) % modulus1

                rolling2 = (rolling2 - (ord(s[i-1])-ord('a'))*power2) % modulus2
                rolling2 = (rolling2*base2 + ord(s[i+target_len-1])-ord('a')) % modulus2

            if (rolling1, rolling2) in hashset:
                # print(i, target_len, len(s))
                return s[i:i+target_len]
            else:
                hashset.add((rolling1, rolling2))
        return ""
