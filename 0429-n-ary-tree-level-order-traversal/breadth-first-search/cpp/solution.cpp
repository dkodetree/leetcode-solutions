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
    vector<vector<int>> levelOrder(Node* root) {
        if (!root) {
            return {};
        }

        vector<vector<int>> result;
        queue<Node*> q;
        q.push(root);

        while (!q.empty()) {
            int level_size = q.size();
            vector<int> level_res;

            for (int i = 0; i < level_size; i++) {
                Node* node = q.front();
                q.pop();
                level_res.push_back(node->val);

                for (Node* child : node->children) {
                    if (child) q.push(child);
                }
            }
            result.push_back(level_res);
        }
        return result;
    }
};
