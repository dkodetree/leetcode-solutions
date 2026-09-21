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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;

        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.push(root);
        
        while (!stack.isEmpty()) {
            TreeNode cur = stack.pop();
            if (cur != null) {
                result.add(cur.val); 
                if (cur.left != null)  stack.push(cur.left);    // Push left first so that right sits on top and gets popped/processed first
                if (cur.right != null) stack.push(cur.right);
            }
        }
        
        Collections.reverse(result); // Reverse to convert root-right-left into left-right-root (i.e. postorder)
        return result;
    }
}
