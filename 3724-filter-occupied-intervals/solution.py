class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals = sorted(occupiedIntervals, key=lambda interval: (interval[0], interval[1]))
        merged_intervals = []
        curr_start, curr_end = occupiedIntervals[0]
        i = 1
        for i in range(len(occupiedIntervals)):
            next_start, next_end = occupiedIntervals[i]
            if curr_end + 1 >= next_start:
                if curr_end <= next_end:
                    curr_end = next_end
            else:
                merged_intervals.append([curr_start, curr_end])
                curr_start, curr_end = next_start, next_end
            if i == len(occupiedIntervals) - 1:
                merged_intervals.append([curr_start, curr_end])
        # print('---merged interval', merged_intervals)
        remaining_intervals = []
        for start, end in merged_intervals:
            if freeStart <= start and start <= freeEnd and freeEnd <= end:
                if freeEnd + 1 <= end:
                    remaining_intervals.append([freeEnd+1, end])
            elif start <= freeStart and freeStart <= end and end <= freeEnd:
                if start <= freeStart-1:
                    remaining_intervals.append([start, freeStart-1])
            elif freeStart <= start and end <= freeEnd:
                pass
            elif start <= freeStart and freeEnd <= end:
                # print(start, end, freeStart, freeEnd)
                if start <= freeStart - 1:
                    remaining_intervals.append([start, freeStart-1])
                if freeEnd + 1 <= end:
                    remaining_intervals.append([freeEnd+1, end])
            else:
                remaining_intervals.append([start, end])
        return remaining_intervals


