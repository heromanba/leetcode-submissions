class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        diff = [0 for _ in range(length)]
        for start, end, inc in updates:
            diff[start] += inc
            if end+1 < length:
                diff[end+1] -= inc
        prefix = [0 for _ in range(length)]
        for i in range(length):
            if i == 0:
                prefix[0] = diff[0]
            else:
                prefix[i] = prefix[i-1] + diff[i]
        return prefix
