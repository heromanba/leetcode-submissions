class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unbalance = []
        for i in s:
            if not unbalance:
                unbalance.append(i)
            else:
                if (i == ")") and (unbalance[-1] == "("):
                    unbalance.pop()
                else:
                    unbalance.append(i)
        return len(unbalance)
