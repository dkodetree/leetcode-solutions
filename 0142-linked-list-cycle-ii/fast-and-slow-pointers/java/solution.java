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
        ListNode slow = head;
        ListNode fast = head;
        // Step 1: Detect the cycle
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                break; // Cycle detected
            }
        }

        if (fast == null || fast.next == null) {
            return null;    // No cycle
        }

        // Step 2: Find the start node of the cycle
        ListNode slow1 = head;
        while (slow != slow1) {
            slow = slow.next;
            slow1 = slow1.next;
        }
        return slow;
    }
}
