class Solution {
public:
    string createHist(string& s) {
        vector<int> hist(26);
        for (auto ch : s) {
            hist[ch-'a']++;
        }
        string strHist = to_string(hist[0]);
        for (int i=1; i<26; i++){
            strHist.append(",");
            strHist.append(to_string(hist[i]));
        }
        return strHist;
    }
    
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;
        for (auto str : strs){
            string hist = createHist(str);
            res[hist].push_back(str);
        }
        vector<vector<string>> ans;
        for (auto resEntry : res){
            ans.push_back(resEntry.second);
        }
        return ans;
    }
};
