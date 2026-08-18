class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> answer(nums);
        for (const auto i : nums)
        {
            answer.push_back(i);
        }
        return answer;
    }
};