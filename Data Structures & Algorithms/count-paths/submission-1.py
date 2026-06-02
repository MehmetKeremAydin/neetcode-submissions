class Solution:
    def factorial(self, n:int)->int:
        if n<=1:
            return 1
        return n * self.factorial(n-1)
    def uniquePaths(self, m: int, n: int) -> int:
        down = m-1
        right = n-1
        return self.factorial(down+right) // (self.factorial(down) * self.factorial(right))
        