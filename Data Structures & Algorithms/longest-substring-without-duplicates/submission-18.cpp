class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> last_seen;
        int best = 0, left = 0;
        for (int right = 0; right < (int)s.size(); right++) {
            auto it = last_seen.find(s[right]);
            if (it != last_seen.end() && it->second >= left) {
                left = it->second + 1;
            }
            last_seen[s[right]] = right;
            best = max(best, right - left + 1);
        }
        return best;
    }
};