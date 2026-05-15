class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, pair<int, int>> graph;
        int n = nums.size(), max_len = 0;
        for (const auto& num : nums)
        {
            int left, right;
            if(graph.contains(num)) continue;
            if(graph.contains(num-1))
                left = graph.at(num-1).first + 1;
            else left = 0;
            if(graph.contains(num+1))
                right = graph.at(num+1).second + 1;
            else right = 0;
            if(right != 0)  graph.at(num+right).first = (left + right);
            if(left != 0) graph.at(num-left).second = (left + right);
            int cur_len = left + right + 1;
            if(cur_len > max_len) max_len = cur_len;
            pair<int, int> data = {left, right};
            graph.insert({num, data});
        }
        return max_len;
    }
};
