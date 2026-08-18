class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> mem;
        for (const auto n : nums){
            if (mem.contains(n)) return true;
            mem.insert(n);
        }
        return false;
    }
};