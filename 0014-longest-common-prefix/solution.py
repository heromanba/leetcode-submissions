class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min([len(s) for s in strs])
        prefix = ""
        for i in range(min_len):
            if len(set([s[i] for s in strs])) == 1:
                prefix += strs[0][i]
            else:
                break
        return prefix
