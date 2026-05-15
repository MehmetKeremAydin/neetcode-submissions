class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, int>> combined(n);
        for (int i = 0; i < n; i++) combined[i] = {position[i], speed[i]};
        sort(combined.begin(), combined.end(), std::greater<>());
        float worst_t = (float)(target - combined[0].first) / (float)combined[0].second;
        int num_fleets = 1;
        for (int i=0; i<n; i++) {
            float best_t = (float)(target - combined[i].first) / (float)combined[i].second;
            //cout<<"best_t: "<<best_t<<" worst_t: "<<worst_t<<endl;
            if (best_t > worst_t) {
                num_fleets++;
                worst_t = best_t;
            }
        }
        return num_fleets;
        
    }
};
