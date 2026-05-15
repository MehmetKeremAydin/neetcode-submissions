class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int maxP = 0;
        for(const auto& pile : piles) maxP = max(maxP, pile);
        int slow = 1, fast = maxP;
        int minViab = fast;
        while (slow<=fast) {
            int medium = (slow + fast) / 2;
            int time = 0;
            for(const auto& pile : piles) time += pile / medium + (pile % medium != 0);
            if (time <= h) {
                minViab = min(minViab, medium);
                fast = medium - 1;
            }
            else slow = medium + 1;
        }
        return minViab;
    }
};
