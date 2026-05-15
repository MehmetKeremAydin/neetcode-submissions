class MinStack {
private:
    stack<int> numStorage, minStorage;
public:
    MinStack() {}
    
    void push(int val) {
        numStorage.push(val);
        if (minStorage.size() > 0) minStorage.push(min(minStorage.top(), val));
        else minStorage.push(val);
    }
    
    void pop() {
        numStorage.pop();
        minStorage.pop();
    }
    
    int top() {
        return numStorage.top();
    }
    
    int getMin() {
        return minStorage.top();
    }
};
