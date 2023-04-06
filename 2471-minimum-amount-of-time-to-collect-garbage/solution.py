class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        time = 0
        travel = [0] + travel
        for l in ["M", "P", "G"]:
            tmp_time = 0
            for i in range(len(garbage)):
                g = garbage[-i-1]
                if l in g:
                    tmp_time += g.count(l)
                    tmp_time += travel[-i-1]
                else:
                    if tmp_time > 0:
                        # farther place has garbage
                        tmp_time += travel[-i-1]
            time += tmp_time
        return time

