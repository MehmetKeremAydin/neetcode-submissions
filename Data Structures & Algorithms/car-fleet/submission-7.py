class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d2tTime = [(target-pos, (target-pos)/spd) for pos, spd in zip(position, speed)]
        d2tTime = sorted(d2tTime)
        numGroups = 0
        worstTimeSoFar = 0
        for entry in d2tTime:
            if entry[1] > worstTimeSoFar:
                numGroups += 1
                worstTimeSoFar = entry[1]
        return numGroups