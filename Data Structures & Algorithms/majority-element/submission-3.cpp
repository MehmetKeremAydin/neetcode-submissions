class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int curNum = nums[0], curCount = 1;
        for (auto n : nums){
            if (n == curNum) curCount++;
            else {
                curCount--;
                if (curCount == 0) {
                    curNum = n;
                    curCount = 1;
                }
            }
        }
        return curNum;
    }
};