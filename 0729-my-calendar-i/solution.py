import bisect

class MyCalendar:

    def __init__(self):
        self.events = []
        self.prefix = []

    def book(self, startTime: int, endTime: int) -> bool:
        # print('---------------------------')
        # print(startTime)
        # print(self.events)
        # print(self.prefix)
        if len(self.events)>0 and \
            not (startTime > self.events[-1][0] or endTime <= self.events[0][0]):
            start_idx = bisect.bisect_left(self.events, startTime, key=lambda x:x[0])
            # print('start_idx', start_idx)
            if start_idx > 0 and self.events[start_idx][0] > startTime:
                start_idx -= 1
            for ev, pre in zip(self.events[start_idx:], self.prefix[start_idx:]):
                if ev[0] >= endTime:
                    break
                if pre + 1 > 1:
                    return False
        self.events.append([startTime, 1])
        self.events.append([endTime,-1])
        self.rebuild_prefix()
        return True
    
    def rebuild_prefix(self):
        tmp_events = sorted(self.events)
        self.events = []
        self.prefix = []
        for ev in tmp_events:
            if len(self.events) > 0 and ev[0] == self.events[-1][0]:
                self.events[-1][1] += ev[1]
            else:
                self.events.append(ev)
        for ev in self.events:
            if len(self.prefix) == 0:
                self.prefix.append(ev[1])
            else:
                self.prefix.append(self.prefix[-1]+ev[1])
        




# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
