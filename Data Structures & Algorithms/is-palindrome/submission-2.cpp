class Solution {
public:
    bool isPalindrome(string s) {
        int cur_begin = 0, cur_end = s.size() - 1;
        for (auto& x : s) {
            x = tolower(x);
        }
        while(cur_begin < cur_end){
            while(!isalnum(s[cur_begin])) cur_begin++;
            while(!isalnum(s[cur_end])) cur_end--;
            if(cur_begin > cur_end) return true;
            if(s[cur_begin] == s[cur_end]){
                cur_begin++;
                cur_end--;
            }
            else return false;
        }
        return true;
    }
};
