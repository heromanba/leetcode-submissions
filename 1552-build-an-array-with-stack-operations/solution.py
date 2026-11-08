class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        results = []
        for i in range(len(target)):
            if i == 0:
                for j in range(1, target[0]):
                    results.append("Push")
                    results.append("Pop")
                results.append("Push")
            else:
                for j in range(target[i-1]+1, target[i]):
                    results.append("Push")
                    results.append("Pop")
                results.append("Push")
        return results

