class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> nums_seen;
        for(uint i=0; i<nums.size(); i++)
        {
            if(nums_seen.contains(nums[i])) return true;
            else nums_seen.insert(nums[i]);
        }
        return false;
    }
};