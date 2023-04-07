class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        start = 0
        while len(friends) > 1:
            end = (start + (k - 1)) % len(friends)
            friends.pop(end)
            start = end
        return friends[0]

