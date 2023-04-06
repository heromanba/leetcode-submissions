class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        count = [None] * len(s)
        for i in range(len(s)):
            tmp_s = s[-i-1:]   
            cnt = 0 
            y, x = startPos
            for act in tmp_s:
                if act == "R":
                    x += 1
                elif act == "D":
                    y += 1
                elif act == "L":
                    x -= 1
                elif act == "U":
                    y -= 1
                if x < 0 or x >= n or y < 0 or y >= n:
                    break
                else:
                    cnt += 1
            count[-i-1] = cnt
        return count
