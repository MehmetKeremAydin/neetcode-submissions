class Solution {
    public:
        vector<int> topKFrequent(vector<int>& nums, int k) {
                unordered_map<int,int> counter;
                vector<unordered_set<int>> bucket(nums.size());
                vector<int> answer;
                int n = nums.size();
                for(int num : nums)
                {
                        counter[num]++;
                }
                for(auto it = counter.begin(); it != counter.end(); it++)
                {
                        int num = it->first;
                        int count = it -> second;
                        bucket[count-1].insert(num);
                }
                for(int i=bucket.size()-1; i>=0; i--)
                {
                        if(bucket[i].empty()) continue;
                        for (auto it = bucket[i].begin(); it != bucket[i].end(); it++)
                        {
                                answer.push_back(*it);
                                if(answer.size() >= k) return answer;
                        }
                }
                return answer;
        }

};
                                                                                                                                                                            