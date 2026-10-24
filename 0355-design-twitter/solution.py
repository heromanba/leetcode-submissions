import heapq
class Twitter:

    def __init__(self):
        self.post_seq = 1
        self.posts = dict()
        self.follows = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.posts:
            self.posts[userId].append((self.post_seq, tweetId))
        else:
            self.posts[userId] = [(self.post_seq, tweetId)]
        self.post_seq += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # print(self.posts)
        iterators = []
        if userId in self.posts and len(self.posts[userId]) > 0:
            iterators.append(reversed(self.posts[userId]))
        if userId in self.follows:
            for followeeId in self.follows[userId]:
                if followeeId in self.posts and len(self.posts[followeeId]) > 0:
                    iterators.append(reversed(self.posts[followeeId]))
        feeds = []
        candidates = []
        for idx, iterator in enumerate(iterators):
            seq_id, tweetId = next(iterator)
            heapq.heappush(candidates, (-seq_id, tweetId, idx))
        while candidates and len(feeds) < 10:
            seq_id, tweetId, iter_idx = heapq.heappop(candidates)
            feeds.append(tweetId)
            try:
                seq_id, tweetId = next(iterators[iter_idx])
                heapq.heappush(candidates, (-seq_id, tweetId, iter_idx))
            except StopIteration:
                continue
        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = { followeeId }

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
