class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char, int> letters_s, letters_t;
        for (uint i=0; i<s.size(); i++)
        {
            if(letters_s.find(s[i]) != letters_s.end()) letters_s.at(s[i])++;
            else letters_s.insert({s[i], 1});
            if(letters_t.find(t[i]) != letters_t.end()) letters_t.at(t[i])++;
            else letters_t.insert({t[i], 1});
        }
        if(letters_s == letters_t) return true;
        return false;
    }
};
