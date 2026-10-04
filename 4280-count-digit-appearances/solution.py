class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        ans = 0
        for n in nums:
            for c in str(n):
                if c == str(digit):
                    ans+=1
        return ans

