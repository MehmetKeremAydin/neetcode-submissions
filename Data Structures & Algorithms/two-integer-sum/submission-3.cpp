class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mem;
        for (int i = 0; i < nums.size(); i++) {
            int t = target - nums[i];
            if (mem.contains(t)) {
                vector<int> answer = {mem[t], i};
                return answer;
            }
            else {
                mem.insert({nums[i], i});
            }
        }
        vector<int> answer = {-1, -1};
        return answer;
    }
};
