class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        for i in range((len(filtered)+1)//2):
            if filtered[i] != filtered[-i-1]:
                return False
        return True
