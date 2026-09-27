class MyCalendarThree:

    def __init__(self):
        self.events = []
        self.prefix = []

    def book(self, startTime: int, endTime: int) -> bool:
        self.events.append([startTime, 1])
        self.events.append([endTime,-1])
        self.rebuild_prefix()
        
        # print('----------------------')
        # print(self.events)
        # print(self.prefix)
        k = 0
        if len(self.events)>0 and \
            not (startTime > self.events[-1][0] or endTime <= self.events[0][0]):
            start_idx = 0#bisect.bisect_left(self.events, startTime, key=lambda x:x[0])
            # print('start_idx', start_idx)
            if start_idx > 0 and self.events[start_idx][0] > startTime:
                start_idx -= 1
            for ev, pre in zip(self.events[start_idx:], self.prefix[start_idx:]):
                # if ev[0] >= endTime:
                #     break
                k = max(k, pre)
        return k
    
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
        



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
