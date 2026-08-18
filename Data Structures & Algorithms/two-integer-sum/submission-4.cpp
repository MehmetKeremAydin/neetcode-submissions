class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mem;
        for (int i = 0; i < nums.size(); i++) {
            int t = target - nums[i];
            if (mem.contains(t)) return {mem[t], i};
            mem.insert({nums[i], i});
        }
        return {-1, -1};
    }
};
