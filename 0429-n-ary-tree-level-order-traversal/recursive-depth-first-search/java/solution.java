/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(root, 0, res);
        return res;
    }

    private void dfs(Node node, int level, List<List<Integer>> res) {
        if (node == null) {
            return;
        }

        if (res.size() == level) {
            res.add(new ArrayList<>());
        }

        res.get(level).add(node.val);

        if (node.children != null) {
            for (Node child : node.children) {
                dfs(child, level + 1, res);
            }
        }
    }
}
