/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // Status Constants
    private final int HAS_CAM = 1;     // node has a camera
    private final int COVERED = 2;     // node is covered (by child)
    private final int NEEDS_COV = 3;   // node is not covered
    
    private int cameras = 0;   // camera counter

    public int minCameraCover(TreeNode root) {
        cameras = 0;
        return dfs(root) == NEEDS_COV ? cameras + 1 : cameras;
    }

    private int dfs(TreeNode node) { 
        // Null nodes are automatically covered
        if (node == null) {
            return COVERED;
        }

        // Postorder traversal - so process children first
        int leftStatus = dfs(node.left); 
        int rightStatus = dfs(node.right); 

        // If any child needs camera, then place camera at current node
        if (leftStatus == NEEDS_COV || rightStatus == NEEDS_COV) { 
            cameras++;
            return HAS_CAM;
        }
        // If any child has camera, then current node is already covered
        if (leftStatus == HAS_CAM || rightStatus == HAS_CAM) { 
            return COVERED;
        }
        // Otherwise current node is not covered
        return NEEDS_COV;
    }
}
