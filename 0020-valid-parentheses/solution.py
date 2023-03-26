class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        close_to_open = dict((v, k) for k, v in open_to_close.items())
        stack = []
        for c in s:
            if c in open_to_close:
                stack.append(c)
            else:
                if not stack:
                    return False
                actual_open = stack.pop()
                expect_open = close_to_open[c]
                if actual_open != expect_open:
                    return False
        if stack:
            return False
        return True
