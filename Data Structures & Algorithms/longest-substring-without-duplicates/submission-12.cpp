class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> last_seen;
        int cur = 0, n=s.size(), max_len = 0;
        if(n == 0 || n == 1) return n;
        for(int i=0; i<=n; i++) {
            if (i == n) {
                int len = i - cur;
                if(len > max_len) return len;
                else return max_len;
            }
            else if (!last_seen.contains(s[i])) {
                last_seen.insert({s[i], i});
                cout<<"inserted "<<s[i]<<" at "<<i<<endl;
            }
            else {       
                int len = i - cur;
                cout<<"Duplicate at "<<i<<" length: "<<len<<endl;
                if (len>max_len) max_len = len;
                int pop_until = last_seen.at(s[i]);
                cout<<"popping until "<<pop_until<<" from "<<cur<<endl;
                while (cur <= pop_until) {
                    cout<<"Popped "<<s[cur]<<endl;
                    last_seen.erase(s[cur]);
                    cur++;
                }
                cout<<"reinserted "<<s[i]<<" at "<<i<<endl;
                last_seen.insert({s[i], i});
            }
        }
        return max_len;
    }
};
