/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> visited = new HashSet<>();
        ListNode cur = head;

        while (cur != null) {
            if (visited.contains(cur)) {
                return true;
            }
            visited.add(cur);
            cur = cur.next;
        }
        return false;
    }
}
