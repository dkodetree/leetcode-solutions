/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) 
            return res;
        
        queue<TreeNode*> node_queue;
        node_queue.push(root);

        while (!node_queue.empty()) {
            int levelSize = node_queue.size();
            vector<int> currentLevel;

            for (int i = 0; i < levelSize; i++) {
                TreeNode* node = node_queue.front();
                node_queue.pop();

                if (node->left) 
                    node_queue.push(node->left);
                if (node->right)
                    node_queue.push(node->right);
                
                currentLevel.push_back(node->val);
            }
            res.push_back(currentLevel);
        }
        return res;
    }
};
