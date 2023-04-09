class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            key_idx = 0
        elif ruleKey == "color":
            key_idx = 1
        elif ruleKey == "name":
            key_idx = 2
        cnt = 0
        for item in items:
            if item[key_idx] == ruleValue:
                cnt += 1
        return cnt
