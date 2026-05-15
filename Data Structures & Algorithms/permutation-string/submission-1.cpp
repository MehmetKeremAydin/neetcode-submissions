class Solution {
public:
    vector<int> createHist(const string& s) {
        int n = s.size();
        vector<int> histogram(26, 0);
        for (int i=0; i<n; i++) {
            histogram[(int)s[i] - 'a']++;
        }
        return histogram;
    }

    bool checkInclusion(string s1, string s2) {
        int n_s1 = s1.size(), n_s2 = s2.size();
        vector<int> baseHist = createHist(s1), testHist = createHist(s2.substr(0, n_s1));
        for (int i=0; i<n_s2-n_s1; i++) {
            if (baseHist == testHist) return true;
            testHist[(int)s2[i] - 'a']--;
            testHist[(int)s2[i+n_s1] - 'a']++;
        }
        if (baseHist == testHist) return true;
        return false;
    }
};
