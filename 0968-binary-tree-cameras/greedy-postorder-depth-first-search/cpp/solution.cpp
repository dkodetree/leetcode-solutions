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
    int minCameraCover(TreeNode* root) {
        int cameras = 0;
        return dfs(root, cameras) == NEEDS_COV ? cameras + 1 : cameras;
    }

private:
    // Status Constants
    static const int HAS_CAM = 1;     // node has a camera
    static const int COVERED = 2;     // node is covered (by child)
    static const int NEEDS_COV = 3;   // node is not covered

    // Greedy Post order DFS
    int dfs(TreeNode* node, int& cameras) {
        // Null nodes are automatically covered
        if (!node) {
            return COVERED;
        } 

        // Postorder traversal - so process children first
        int left_status = dfs(node->left, cameras); 
        int right_status = dfs(node->right, cameras); 

        // If any child needs camera, then place camera at current node
        if (left_status == NEEDS_COV || right_status == NEEDS_COV) { 
            cameras++; 
            return HAS_CAM; 
        }
        // If any child has camera, then current node is already covered
        if (left_status == HAS_CAM || right_status == HAS_CAM) { 
            return COVERED; 
        }
        // Otherwise node is not covered
        return NEEDS_COV; 
    }
};
