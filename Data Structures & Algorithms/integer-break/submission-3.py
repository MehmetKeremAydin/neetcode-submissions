class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {2:2, 3:3, 4:4, 5:6}
        edge = {2:1, 3:2}
        if n in edge:
            return edge[n]
        if n <= 5:
            return dp[n]
        for i in range(6, n+1):
            dp[i] = max([dp[i-j]*j for j in range(2,4)])
        return dp[n]
        