class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for s in strs:
            counter = {}
            for c in s:
                if c in counter:
                    counter[c] += 1
                else:
                    counter[c] = 0
            anagram_key = tuple(sorted([(k,v) for k,v in counter.items()], key=lambda item: item[0]))
            if anagram_key not in anagram_groups:
                anagram_groups[anagram_key] = [ s ]
            else:
                anagram_groups[anagram_key].append(s)
        return list(anagram_groups.values())
