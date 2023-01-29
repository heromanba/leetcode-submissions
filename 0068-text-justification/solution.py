class Solution:
    def packWords(self, words: List[str], maxWidth: int) -> str:
        if len(words) == 1:
            # left justify for just one word
            return words[0] + " " * (maxWidth - len(words[0]))
        else:
            wordsLen = len("".join(words))
            interval = len(words) - 1
            numSpace = (maxWidth - wordsLen) // interval
            numExtraSpace = (maxWidth - wordsLen) % interval
            ret = ""
            for i in range(interval):
                if i < numExtraSpace:
                    ret += words[i] + " " + " " * numSpace
                else:
                    ret += words[i] + " " * numSpace
            ret += words[-1]
            return ret
    
    def cost(self, i, j, words, maxWidth):
        ijLen = len(" ".join(words[i:j]))
        if ijLen > maxWidth:
            return float('inf')
        else:
            # greedy: longer -> better
            # print(i, j, words[i:j], maxWidth, - (j - i))
            return - (j - i)
    
    def dp(self, i, words, maxWidth):
        if i in self.dpTable:
            return self.dpTable[i]
        if i == len(words):
            return 0
        min = float('inf')
        argMin = None
        for j in range(i+1, len(words)+1):
            cur = self.cost(i, j, words, maxWidth) + self.dp(j, words, maxWidth)
            if cur <= min:
                min = cur
                argMin = j
        self.child[i] = argMin
        self.dpTable[i] = min
        return min

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        self.child = {}
        self.dpTable = {}
        self.nLines = 0

        ret = []
        tmp = []
        
        self.dp(0, words, maxWidth)
        results = []
        i = 0
        while self.child[i] < len(words):
            # print(i, self.child[i], len(words), words)
            results.append(self.packWords(words[i:self.child[i]], maxWidth))
            i = self.child[i]

        # last line left justify
        tmpStr = " ".join(words[i:self.child[i]])
        tmpStr += " " * (maxWidth - len(tmpStr))
        results.append(tmpStr)
        return results
