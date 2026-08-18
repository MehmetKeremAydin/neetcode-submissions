class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> hist(26);
        for (auto ch : s) hist[ch-'a'] += 1;
        for (auto ch : t) hist[ch-'a'] -= 1;
        for (const auto i : hist){
            if (i != 0) {
                return false;
            }
        }
        return true;
    }   
};
