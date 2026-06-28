class Solution:
    def maxDistance(self, moves: str) -> int:
        cnt = 0
        src = [0, 0]
        for c in moves:
            if c == 'U':
                src[1]+=1
            elif c == 'D':
                src[1]-=1
            elif c == 'L':
                src[0] -= 1
            elif c == 'R':
                src[0] += 1
            elif c == '_':
                cnt+=1
        return abs(src[0]) + abs(src[1]) + cnt

