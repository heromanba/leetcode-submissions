class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x: x)
        days_with_meeting = 0
        curr_start = None
        curr_end = None
        for i in range(len(meetings)):
            if curr_start is None:
                curr_start, curr_end = meetings[i]
            if curr_start <= meetings[i][0] and meetings[i][0] <= curr_end and meetings[i][1] >= curr_end:# with overlap
                curr_end = meetings[i][1]
            elif curr_end < meetings[i][0]:
                # no overlap
                days_with_meeting += (curr_end-curr_start+1)
                curr_start, curr_end = meetings[i]

            if i == len(meetings) - 1:
                days_with_meeting += (curr_end-curr_start+1)
        return days - days_with_meeting
