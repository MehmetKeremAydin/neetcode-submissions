class Solution {
public:
    bool isValid(string s) {
        stack<char> storage;
        for(const auto& entry : s) {
            if(entry == '(' || entry == '{' || entry == '[') storage.push(entry);
            else {
                if (storage.size() == 0) return false;
                else if (entry == ')' && storage.top() != '(') return false;
                else if (entry == '}' && storage.top() != '{') return false;
                else if (entry == ']' && storage.top() != '[') return false;
                else storage.pop();
            }
        }
        if (storage.size() != 0) return false;
        else return true;
    }
};
