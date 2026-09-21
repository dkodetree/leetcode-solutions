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
    vector<int> postorder(Node* root) {
        vector<int> result;
        stack<Node*> stk;
        stk.push(root);

        while (!stk.empty()) {
            Node* node = stk.top();
            stk.pop();

            if (node) {
                result.push_back(node->val);
                // Push children left-to-right so that rightmost child stays on top and pops first
                for (Node* child : node->children) {
                    if (child) {
                        stk.push(child);
                    }
                }
            }
        }

        // Reverse to convert [Root -> Rightmost ... Leftmost] into  [Leftmost ... Rightmost -> Root] (i.e. postorder)
        reverse(result.begin(), result.end());
        return result;
    }
};
