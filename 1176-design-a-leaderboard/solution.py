import heapq

class Leaderboard:

    def __init__(self):
        self.scores = dict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            self.scores[playerId] += score
        else:
            self.scores[playerId] = score

    def top(self, K: int) -> int:
        return sum(sorted(self.scores.values(), reverse=True)[:K])
        

    def reset(self, playerId: int) -> None:
        self.scores.pop(playerId, None)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
