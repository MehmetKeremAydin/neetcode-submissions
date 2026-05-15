class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        int n = nums.size();
        vector<int> zero_idx;
        vector<int> answer(nums.size(), 0);
        for(int i=0; i<n; i++)
        {
            if(nums[i] != 0) product *= nums[i];
            else zero_idx.push_back(i);
        }
        if(zero_idx.size() == 0)
        {
            for(int i=0; i<n; i++) answer[i] = product / nums[i]; 
        }
        else if(zero_idx.size() == 1)
        {
            cout<<zero_idx[0]<<endl;
            answer[zero_idx[0]] = product;
        }
        return answer;
    }
};
