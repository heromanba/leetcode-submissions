class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(1, len(digits)+1):
            d = digits[-i]
            if d >= 10:
                digits[-i] = d % 10
                if (i+1) > len(digits):
                    return [1] + digits
                else:
                    digits[-i-1] += 1
            else:
                digits[-i] = d
        return digits
