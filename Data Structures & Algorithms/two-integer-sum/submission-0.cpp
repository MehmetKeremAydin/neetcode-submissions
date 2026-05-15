class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> sub;
        vector<int> answer;
        for(uint i=0; i<nums.size(); i++)
        {
            if(sub.contains(nums[i]))
            {
                answer.push_back(sub[nums[i]]);
                answer.push_back(i);
                return answer;
            }
            else sub.insert({target-nums[i], i});
        }
    }
};
