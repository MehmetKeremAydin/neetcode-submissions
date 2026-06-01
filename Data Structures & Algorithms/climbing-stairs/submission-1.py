class Solution:
    def climbStairs(self, n: int) -> int:
        def recClimb(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in hashmap:
                return hashmap[n]
            else:
                hashmap[n] = recClimb(n-1) + recClimb(n-2)
            return hashmap[n]
        hashmap = {}
        return recClimb(n)
        