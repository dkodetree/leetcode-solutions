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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        vector<TreeNode*> stack;
        stack.push_back(root);

        while (!stack.empty()) {
            TreeNode* cur = stack.back();
            stack.pop_back();
            if (cur) {
                result.push_back(cur->val);
                stack.push_back(cur->left); // Push left first so that right sits on top and gets popped/processed first
                stack.push_back(cur->right);
            }
        }

        reverse(result.begin(), result.end()); // reverse to convert root-right-left into left-right-root (ie.postorder)
        return result;
    }
};
