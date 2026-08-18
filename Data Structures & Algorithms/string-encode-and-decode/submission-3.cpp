class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded;
        for (auto str : strs){
            encoded.append(to_string(str.size()));
            encoded.append("#");
            encoded.append(str);
        }
        return encoded;
    }

    vector<string> decode(string s) {
        int start = 0;
        vector<string> decoded;
        while (start < s.size()) {
            int headerEnd = s.find("#", start);
            int lenSubStr = stoi(s.substr(start, headerEnd-start));
            decoded.push_back(s.substr(headerEnd+1, lenSubStr));
            start = headerEnd + lenSubStr + 1;
        }
        return decoded;
    }
};
