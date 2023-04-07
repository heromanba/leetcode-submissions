class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        # pattern and word must be one to one mapping
        ret = []
        for word in words:
            mapping = dict()
            match = True
            for w, p in zip(word, pattern):
                # check if word match to pattern correctly
                if (w in mapping) and (mapping[w] != p):
                    match = False
                    break
                mapping[w] = p
            if match:
                # check if pattern match to word correctly
                reverse_mapping = dict()
                for w, p in mapping.items():
                    if p in reverse_mapping:
                        match = False
                        break
                    reverse_mapping[p] = w
            if match:
                # if still matches
                ret.append(word)
        return ret
