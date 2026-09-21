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
        dfs(root, result);
        return result;
    }

private:
    void dfs(Node* node, vector<int>& result) {
        if (node) {
            for (Node* child : node->children) {
                dfs(child, result);
            }
            result.push_back(node->val);
        }
    }
};
