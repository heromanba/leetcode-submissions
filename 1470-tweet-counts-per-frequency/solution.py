class TweetCounts:

    def __init__(self):
        self.tweets = []
        self.changed = False

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets.append((time, tweetName))
        self.changed = True

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> list[int]:
        if self.changed:
            self.tweets = sorted(self.tweets, key=lambda x: x[0])
        # print(freq, tweetName, startTime, endTime, self.tweets)
        if freq == 'minute':
            delta = 60
        elif freq == 'hour':
            delta = 3600
        elif freq == 'day':
            delta = 86400
        i = 0
        ret = []
        for start in range(startTime, endTime+1, delta):
            cnt = 0
            end = min(endTime+1, start + delta)
            # print('start', i, start, end)
            while i < len(self.tweets) and self.tweets[i][0] < end:
                if start <= self.tweets[i][0]:
                    if tweetName in self.tweets[i][1]:
                        cnt += 1
                i += 1
            ret.append(cnt)
        return ret



# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
