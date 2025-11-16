/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;      // Copy next node's value
        node.next = node.next.next;    // Skip next node
        // Java's garbage collector automatically frees memory of the skipped node
    }
}
