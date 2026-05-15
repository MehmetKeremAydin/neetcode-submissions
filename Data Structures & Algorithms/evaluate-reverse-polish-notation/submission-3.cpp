class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int n = tokens.size();
        unordered_set<string> operations = {"+", "-", "*", "/"};
        stack<int> storage;
        for(int i=0; i<n; i++) {
            if (operations.contains(tokens[i])) {
                int num1 = storage.top();
                storage.pop();
                int num2 = storage.top();
                storage.pop();
                if (tokens[i] == "+") storage.push(num2+num1);
                else if (tokens[i] == "-") storage.push(num2-num1);
                else if (tokens[i] == "*") storage.push(num2*num1);
                else storage.push(num2/num1);
            }
            else storage.push(stoi(tokens[i]));
        }
        return storage.top();
    }
};
