class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n in [1,2]:
            return 1
        n_1, n_2, n_3 = 1, 1, 0
        for i in range(n-2):
            nxt = n_1 + n_2 + n_3
            n_1, n_2, n_3 = nxt, n_1, n_2
        return nxt       