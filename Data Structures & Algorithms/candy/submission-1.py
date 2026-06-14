class Solution:
    def candy(self, ratings: List[int]) -> int:
        l2r = [0] * len(ratings)
        r2l = [0] * len(ratings)
        l2r[0] = r2l[-1] = 1
        for i in range(1, len(ratings)):
            l2r[i] = 1 if ratings[i] <= ratings[i-1] else l2r[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            r2l[i] = 1 if ratings[i] <= ratings[i+1] else r2l[i+1] + 1
        return sum([max(l2r[i], r2l[i]) for i in range(len(ratings))])
        