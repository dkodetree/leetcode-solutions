/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> result;
        std::stack<Node*> stk;
        stk.push(root);

        while (!stk.empty()) {
            Node* node = stk.top();
            stk.pop();
            if (node) {
                result.push_back(node->val);
                // Push children in reverse order so that leftmost child is processed first
                for (auto it = node->children.rbegin(); it != node->children.rend(); it++) {
                    stk.push(*it);
                }
            }
        }
        return result;
    }
};
