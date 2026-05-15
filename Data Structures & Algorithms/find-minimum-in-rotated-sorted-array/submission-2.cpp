class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0, r = nums.size() - 1;
        while (r - l > 1) {
            int m = (r + l) / 2;
            if(nums[l] <= nums[m] && nums[m] <= nums[r]) return nums[l];
            else if(nums[l] < nums[m]) l = m + 1;
            else if(nums[m] < nums[r]) r = m;
        }
        return min(nums[r], nums[l]);
    }
};
