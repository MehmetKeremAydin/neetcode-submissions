class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> temp_hist;
        int n=temperatures.size();
        vector<int> answer(n, 0);
        for(int i=0; i<n; i++) {
            while (!temp_hist.empty() && temp_hist.top().first < temperatures[i]) {
                pair<int, int> popped = temp_hist.top();
                temp_hist.pop();
                //cout<<"Popped: "<<popped.first<<" "<<popped.second<<endl;
                answer[popped.second] = i - popped.second;
            }
            pair<int, int> data_point = {temperatures[i], i};
            //<<"Pushed: "<<data_point.first<<" "<<data_point.second<<endl;
            temp_hist.push(data_point);
        }
        return answer;
    }
};
