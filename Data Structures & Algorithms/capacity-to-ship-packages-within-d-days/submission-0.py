class Solution:
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def simShipping(capacity:int):
            days = 1
            usage = 0
            for w in weights:
                usage += w
                if usage > capacity:
                    days += 1
                    usage = w
            return days

        capVsDays = {}
        l = 0
        r = 0
        
        for w in weights:
            l = max(l, w)
            r += w
        answer = r
        while l <= r:
            c = (l + r) // 2
            day = simShipping(c)
            capVsDays[c] = day
            if day <= days:
                r = c - 1
                answer = min(answer, c)
                if answer-1 in capVsDays and capVsDays[answer-1] == days+1:
                    return c
                else:
                    r = c - 1
            elif day > days:
                l = c + 1
        return answer
        