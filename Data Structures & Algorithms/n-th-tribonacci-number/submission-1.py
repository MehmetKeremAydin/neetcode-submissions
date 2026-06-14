class Solution:
    def tribonacci(self, n: int) -> int:
        def trib(k):
            if k in memory:
                return memory[k]
            if k == 0:
                return 0
            if k in [1,2]:
                return 1
            answer = trib(k-1) + trib(k-2) + trib(k-3)
            memory[k] = answer
            return answer
        memory = {}
        return trib(n)
        