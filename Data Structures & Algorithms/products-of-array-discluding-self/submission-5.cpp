class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer(nums.size(), 1);
        int n = nums.size();
        int storage=1;
        for(int i=1; i<n; i++)
            answer[i] = answer[i-1] * nums[i-1];
        for(int i=nums.size()-2; i>=0; i--)
        {
            storage *= nums[i+1];
            answer[i] *= storage;
        }
            
        return answer;
    }
};
