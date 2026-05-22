class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        signN = n / abs(n)
        n = abs(n)
        powers = {1:x}
        rem = n - 1
        i = 1
        while(rem>0):
            i = i + i
            x = x * x
            powers[i] = x
            rem -= i
        cumSum = 0
        total = 1
        while(cumSum != n):
            if cumSum + i <= n:
                total = total * powers[i]
                cumSum = cumSum + i
                if cumSum == n:
                    return total if signN == 1 else 1 / total
            i = i // 2