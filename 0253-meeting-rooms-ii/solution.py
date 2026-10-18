class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append([start, 1])
            events.append([end, -1])
        events = sorted(events)
        prefix = []
        max_overlap = 0
        for ev in events:
            if len(prefix) == 0:
                prefix.append(ev)
            else:
                prefix.append([ev[0], ev[1]+prefix[-1][1]])
            max_overlap = max(max_overlap, prefix[-1][1])
        return max_overlap

