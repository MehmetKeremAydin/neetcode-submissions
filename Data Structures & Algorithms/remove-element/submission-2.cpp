class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int numValid = 0;
        for (int i=0; i<nums.size(); i++){
            if (nums[i] != val){
                nums[numValid] = nums[i];
                numValid++;
            }
        }
        return numValid;
    }
};