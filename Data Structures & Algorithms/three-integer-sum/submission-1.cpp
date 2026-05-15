class Solution {
public:
    vector<vector<int>> twoSum(const vector<int>& nums, const int& start, const int& target) {
        int n = nums.size();
        vector<vector<int>> answer;
        unordered_set<int> look_up;
        for (int i = start; i<n; i++) {
            if (look_up.contains(target - nums[i]))
            {
                vector<int> solution = {nums[i], target - nums[i]};
                if(count(answer.begin(), answer.end(), solution)) continue;
                answer.push_back(solution);
            }
            else look_up.insert(nums[i]);
        }
        return answer;
    }
    
    
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> answer;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for(int i=0; i<n-2; i++) {
            if(i == 0) {}
            else if(nums[i] == nums[i-1]) continue;
            int target = - nums[i];
            cout<<target<<endl;
            vector<vector<int>> twoSumSolns = twoSum(nums, i+1, target);
            if(twoSumSolns.size() == 0) continue;
            for(auto& solution : twoSumSolns) {
                auto extended = solution;
                extended.push_back(nums[i]);
                answer.push_back(extended);
            }
        }
        
        
        //for(const auto& num : nums) cout<<num<<' ';
        //cout<<endl;
        return answer;
    }
};
