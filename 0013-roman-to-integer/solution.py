class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        for idx, c in enumerate(s):
            if ((c == "I") and (idx + 1 < len(s)) and (s[idx + 1] in ("V", "X"))) \
            or ((c == "X") and (idx + 1 < len(s)) and (s[idx + 1] in ("L", "C"))) \
            or ((c == "C") and (idx + 1 < len(s)) and (s[idx + 1] in ("D", "M"))):
                result -= mapping[c]
            else:
                result += mapping[c]
        return result

                
