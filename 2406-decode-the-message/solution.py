class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        letters = "abcdefghijklmnopqrstuvwxyz"
        mapping = dict()
        i, j = 0, 0
        while i != 26:
            if key[j] not in mapping:
                mapping[key[j]] = letters[i]
                i += 1
            j += 1
        return "".join([mapping[c] if c != " " else c for c in message])
