"""
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

    Twitter() Initializes your twitter object.
    void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
    List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user 
    followed or by the user themself. Tweets must be ordered from most recent to least recent.
    void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
    void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

"""


class Twitter:

    def __init__(self):
        self.users = {}
        self.i = 0
    
    def initUser(self, userId):
        self.users[userId] = {
            "follows": set(),
            "tweets": []
        }

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.initUser(userId)
        self.users[userId]["tweets"].append((-self.i, tweetId))
        self.i += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.initUser(userId)

        h = list(self.users[userId]["tweets"])
        for uid in self.users[userId]["follows"]:
            if uid not in self.users:
                self.initUser(uid)
            h.extend(self.users[uid]["tweets"])

        heapify(h)
        k = 10
        output = []
        while h and k > 0:
            output.append(heappop(h)[1])
            k -= 1
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.initUser(followerId)
        self.users[followerId]["follows"].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.initUser(followerId)
        if followeeId in self.users[followerId]["follows"]:
            self.users[followerId]["follows"].remove(followeeId)
        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
