/*
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> max_left(n, 0), max_right(n, 0);
        int water_capacity = 0;
        for(int i = 1; i<n; i++)
            max_left[i] = max(max_left[i-1], height[i-1]);
        for(int i = n-2; i>=0; i--)
            max_right[i] = max(max_right[i+1], height[i+1]);
        for(int i = 0; i<n; i++)
            water_capacity += max(0,  min(max_left[i], max_right[i])-height[i]);
        
        //for(const auto num : column_capacity) cout<<num<<' ';
        //cout<<endl;
        return water_capacity;
    }
};
*/

class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int max_r = 0;
        vector<int> column_capacity(n,0);
        int water_capacity = 0;
        for(int i = 1; i<n; i++)
            column_capacity[i] = max(column_capacity[i-1], height[i-1]);
        for(int i = n-2; i>0; i--)
        {
            max_r = max(max_r, height[i+1]);
            column_capacity[i] = min(column_capacity[i], max_r);
        }
        for(int i = 1; i<n-1; i++)
            water_capacity += max(0,  column_capacity[i]-height[i]);
        return water_capacity;
    }
};