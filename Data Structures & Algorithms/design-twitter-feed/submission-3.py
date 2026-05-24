class Twitter:

    def __init__(self):
        self.userFollows = {}
        self.userPosts = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.userPosts:
            self.userPosts[userId].append((self.time, tweetId))
        else:
            self.userPosts[userId] = [(self.time, tweetId)]
        self.time += 1
        return
        
    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        if (not userId in self.userPosts) and (not userId in self.userFollows):
            return posts
        if not userId in self.userFollows:
            self.userFollows[userId] = [userId]
        elif not userId in self.userFollows[userId]:
            self.userFollows[userId].append(userId)
        for posterId in self.userFollows[userId]:
            if posterId in self.userPosts:
                posts += self.userPosts[posterId]
        heapq.heapify_max(posts)
        #print(posts)
        recentPosts = []
        while len(recentPosts) < 10 and posts:
            recentPosts.append(heapq.heappop_max(posts)[1])
        #recentPosts.reverse()
        return recentPosts
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollows:
            if followeeId in self.userFollows[followerId]:
                return
            self.userFollows[followerId].append(followeeId)
        else: 
            self.userFollows[followerId] = [followeeId]
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userFollows and followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)
        return
        
