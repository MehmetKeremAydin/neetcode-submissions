class Solution {
public:
    vector<int> getCharHist(string input)
    {
        vector<int> hist(26, 0);
        int n = input.size();
        for(int i = 0; i<n; i++)
        {
            hist[int(input[i]) - int('a')]++;
        }
        return hist;
    }
    
    vector<vector<string>> groupAnagrams(vector<string>& strs) 
    {
        vector<vector<string>> answer;
        map<vector<int>, int> group_table;
        int n = strs.size();
        vector<int> hist;
        for(int i=0; i<n; i++)
        {
            hist = getCharHist(strs[i]);
            if(group_table.contains(hist))
            {
                int idx = group_table[hist];
                answer[idx].push_back(strs[i]);
            }
            else
            {
                vector<string> new_group;
                new_group.push_back(strs[i]);
                answer.push_back(new_group);
                group_table.insert({hist, answer.size()-1});
            }
        }
        return answer;
    }
};
