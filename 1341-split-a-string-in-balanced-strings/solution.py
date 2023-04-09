class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ret = []
        tmp = ""
        for c in s:
            tmp += c
            if (tmp.count("R")==tmp.count("L")):
                ret.append(tmp)
        return len(ret)
