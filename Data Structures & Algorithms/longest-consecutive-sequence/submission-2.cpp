class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set nums_set(nums.begin(), nums.end());
        int max_len = 0;
        for(const auto& number : nums)
        {
            if(nums_set.contains(number-1)) continue;
            int len = 0;
            while(nums_set.contains(number+len)) len++;
            if (len > max_len) max_len = len;
        }
        return max_len;
    }
};
