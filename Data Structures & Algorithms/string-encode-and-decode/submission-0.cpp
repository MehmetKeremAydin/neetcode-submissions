class Solution {
public:

    string createHeader(int length)
    {
        string header = "$";
        header += to_string(length);
        header += "$";
        return header;
    }
    
    string encode(vector<string>& strs) {
        string encoded;
        for(const auto& msg : strs)
        {
            int msg_len = msg.size();
            string header = createHeader(msg_len);
            encoded += header;
            encoded += msg;
        }
        return encoded;
    }
    
    int readHeader(int& i, const string& encoded)
    {
        int end = encoded.find("$", i+1);
        string length_str = encoded.substr(i+1, end-i-1);
        int length = stoi(length_str);
        i = end + 1;
        return length;
    }

    vector<string> decode(string s) {
        vector<string> decoded;
        int msg_len = s.size();
        int cursor = 0;
        while(cursor < msg_len)
        {
            int length = readHeader(cursor, s);
            string sub_msg = s.substr(cursor, length);
            decoded.push_back(sub_msg);
            cursor += length;
        }
        return decoded;
    }
};
