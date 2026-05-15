class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l=0, r=heights.size()-1;
        int max_area = 0;
        while(l < r) {
            int hl = heights[l];
            int hr = heights[r];
            int area = min(hl, hr) * (r - l);
            //cout<<l<<' '<<r<<' '<<hl<<' '<<hr<<endl;
            if (max_area < area) max_area = area;
            if(hl <= hr) l++;
            else r--;
        }
        return max_area;   
    }
};
