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
    public List<Integer> preorder(Node root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;

        Deque<Node> stack = new ArrayDeque<>();
        stack.push(root);

        while (!stack.isEmpty()) {
            Node node = stack.pop();
            result.add(node.val);

            // Push children in reverse order so leftmost child is processed first
            List<Node> children = node.children;
            if (children != null) {
                for (int i = children.size() - 1; i >= 0; i--) {
                    Node child = children.get(i);
                    if (child != null)  stack.push(child);
                }
            }
        }
        return result;
    }
}
