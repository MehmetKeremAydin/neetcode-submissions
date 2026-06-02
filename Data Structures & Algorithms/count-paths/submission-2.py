class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        down = m-1
        right = n-1
        return math.factorial(down+right) // (math.factorial(down) * math.factorial(right))
        