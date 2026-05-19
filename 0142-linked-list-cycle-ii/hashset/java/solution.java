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
    public ListNode detectCycle(ListNode head) {
        HashSet<ListNode> visited = new HashSet<>();
        ListNode cur = head;
        while (cur != null) {
            if (!visited.add(cur)) 
                return cur;     // Cycle entry found
            cur = cur.next;
        }
        return null;            // No cycle
    }
}
