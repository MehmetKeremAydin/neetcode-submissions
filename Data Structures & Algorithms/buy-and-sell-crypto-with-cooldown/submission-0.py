class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def recursiveProfit(i, state):
            if (i, state) in memory: return memory[(i, state)]
            if i >= len(prices):
                return 0
            if state == "buy":
                profit1 = recursiveProfit(i+1, "buy")
                profit2 = recursiveProfit(i+1, "sell") - prices[i]
            elif state == "sell":
                profit1 = recursiveProfit(i+1, "sell")
                profit2 = recursiveProfit(i+2, "buy") + prices[i]
            memory[(i, state)] = max(profit1, profit2)
            return max(profit1, profit2)
        
        memory = {}
        return recursiveProfit(0, "buy")
        