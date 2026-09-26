import bisect

class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        num_open_no_merge = []
        for flower in flowers:
            num_open_no_merge.append([flower[0], 1])
            num_open_no_merge.append([flower[1]+1, -1])
        num_open_no_merge = sorted(num_open_no_merge, key=lambda x: x[0])
        num_open = []
        for item in num_open_no_merge:
            if len(num_open) > 0 and item[0] == num_open[-1][0]:
                num_open[-1][1] += item[1]
            else:
                num_open.append(item)
        prefix_num = []
        for i in range(len(num_open)):
            if i == 0:
                prefix_num.append(num_open[0][1])
            else:
                prefix_num.append(prefix_num[-1] + num_open[i][1])
        ret = []
        # print(num_open)
        # print(prefix_num)
        for ppl in people:
            idx = bisect.bisect_left(num_open, ppl, key=lambda x: x[0])
            # print(ppl, idx, num_open[idx], prefix_num[idx])
            if idx < len(num_open) and num_open[idx][0] == ppl:
                ret.append(prefix_num[idx])
            elif idx == 0 or idx >= len(num_open):
                ret.append(0)
            else:
                ret.append(prefix_num[idx-1])
        return ret
