import bisect
class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        ev_tmp = []
        for first, last, seats in bookings:
            ev_tmp.append([first, seats])
            ev_tmp.append([last+1, -seats])
        ev_tmp = sorted(ev_tmp, key=lambda x:x[0])
        ev = []
        for item in ev_tmp:
            if len(ev) > 0 and item[0] == ev[-1][0]:
                ev[-1][1] += item[1]
            else:
                ev.append(item)
        prefix = [None] * len(ev)
        for i in range(len(prefix)):
            if i == 0:
                prefix[0] = ev[0][1]
            else:
                prefix[i] = prefix[i-1] + ev[i][1]
        ret = []
        for i in range(1,n+1):
            idx = bisect.bisect(ev, i, key=lambda x:x[0])
            # print(ev, i, idx)
            if idx >= len(ev) or ev[idx][0] == 0:
                ret.append(0)
            elif ev[idx][0] == i:
                ret.append(prefix[idx])
            else:
                ret.append(prefix[idx-1])
        return ret

