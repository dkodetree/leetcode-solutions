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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        vector<TreeNode*> stk;
        stk.push_back(root);

        while (!stk.empty()) {
            TreeNode* cur = stk.back();
            stk.pop_back();
            if (cur) {
                result.push_back(cur->val);
                stk.push_back(cur->right);  // Push right first so that left sits on top and gets popped/processed first
                stk.push_back(cur->left);
            }
        }
        return result;
    }
};
