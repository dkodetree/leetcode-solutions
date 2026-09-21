/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        // Dummy node to simplify edge cases
        ListNode dummy = new ListNode(0, head); //dummy on heap
        ListNode leftPrev = dummy;

        // Move leftPrev to the node just before "left"
        for (int i = 0; i < left - 1; i++) {
            leftPrev = leftPrev.next;
        }

        // Reverse sublist from left to right
        ListNode cur = leftPrev.next;
        ListNode prev = null;
        ListNode nxt = null;
        for (int i = 0; i < right - left + 1; i++) {
            nxt = cur.next;
            cur.next = prev;
            prev = cur;
            cur = nxt;
        }

        // Reconnect reversed sublist with the rest
        leftPrev.next.next = nxt; // connect tail of reversed part to the remaining list
        leftPrev.next = prev;      // connect leftPrev to the new head of reversed part
        return dummy.next;
    }
}
