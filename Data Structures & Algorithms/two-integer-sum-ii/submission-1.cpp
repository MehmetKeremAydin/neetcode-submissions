class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l=0, r=numbers.size()-1;
        ;
        while(l < r){
            if(numbers[l] + numbers[r] == target)
            {
                vector<int> answer = {l+1, r+1};
                return answer; 
            }
            else if(numbers[l] + numbers[r] > target) r--;
            else l++;
        }
    }
};
