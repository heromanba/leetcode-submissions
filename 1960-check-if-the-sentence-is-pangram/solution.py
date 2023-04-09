class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        return len(set(alpha).difference(set(sentence))) == 0
