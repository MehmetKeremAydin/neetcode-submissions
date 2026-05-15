class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        slow, fast = 1, max(piles)
        v_eat_min = fast
        while (slow<=fast):
            v_eat = (fast + slow) // 2
            time = 0
            for pile in piles:
                time +=  math.ceil(pile/v_eat)
            if time <= h:
                v_eat_min = min(v_eat_min, v_eat)
                fast = v_eat - 1
            else:
                slow = v_eat + 1
        return v_eat_min
        