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
}
*/

class Solution {
    public List<Integer> postorder(Node root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        
        Deque<Node> stack = new ArrayDeque<>();
        stack.push(root);

        while (!stack.isEmpty()) {
            Node node = stack.pop();

            if (node != null) {
                result.add(node.val);
                if (node.children != null) {
                    // Push children left-to-right so that rightmost child stays on top and pops first
                    for (Node child : node.children) {
                        if (child != null)  stack.push(child);
                    }
                }
            }
        }

        // Reverse to convert [Root -> Rightmost ... Leftmost] into [Leftmost ... Rightmost -> Root] (i.e. postorder)
        Collections.reverse(result);
        return result;
    }
}
