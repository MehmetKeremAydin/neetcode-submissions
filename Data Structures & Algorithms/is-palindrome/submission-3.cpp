class Solution {
public:
    bool isPalindrome(string s) {
        int cur_begin = 0, cur_end = s.size() - 1;
        while(cur_begin < cur_end){
            while(cur_begin < cur_end &&!isalnum(s[cur_begin])) cur_begin++;
            while(cur_begin < cur_end &&!isalnum(s[cur_end])) cur_end--;
            if(cur_begin > cur_end) return true;
            if(tolower(s[cur_begin]) == tolower(s[cur_end])){
                cur_begin++;
                cur_end--;
            }
            else return false;
        }
        return true;
    }
};
