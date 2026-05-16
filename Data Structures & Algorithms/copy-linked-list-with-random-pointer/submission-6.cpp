/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> conns;
        Node* cur = head;
        // First pass
        while(cur) {
            Node *newNode = new Node(cur->val);
            conns[cur] = newNode;
            cur = cur->next;
        }
        cur = head;
        // Second pass
        while(cur) {
            Node *newNode = conns[cur];
            newNode->next = conns[cur->next];
            newNode->random = cur->random ? conns[cur->random] : nullptr;
            cur = cur->next;
        }
        return conns[head];
    }
};
