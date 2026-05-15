class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int b = 0, s = 1, n = prices.size();
        int profit = 0, max_profit=0;
        for(; s<n; s++)
        {
            if(prices[b] < prices[s]) 
            {
                profit = prices[s] - prices[b];
                if(max_profit < profit) max_profit = profit;
            }
            else b=s;
        }
        return max_profit;
    }
};
