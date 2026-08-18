class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> hist;
        for (auto n : nums){
            hist[n]++;
        }
        priority_queue<pair<int, int>> shist;
        for (auto dataPair : hist){
            shist.push({dataPair.second, dataPair.first});
        }
        vector<int> res;
        for (int i=0; i<k; i++) {
            res.push_back(shist.top().second);
            shist.pop();
        }
        return res;
    }
};
