//ABBCCABCCA
class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.size();
        int non_tar_char_cnt;
        int best = 0;
        for (int i='A'; i<='Z'; i++) {
            int l = 0;
            non_tar_char_cnt = 0;
            for(int r = 0; r<n; r++) {
                if (i != (int)s[r]) non_tar_char_cnt ++;
                while(non_tar_char_cnt > k) {
                    if (i != (int)s[l]) non_tar_char_cnt --;
                    l++;
                }
                int len = r - l + 1;
                best = max(len, best);
            }
        }
        return best;
    }
};
