/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head;
        ListNode *fast = head;

        // Step 1: Detect the cycle
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                break; // Cycle detected
            }
        }

        if (!fast || !fast->next) { 
            return nullptr; // No cycle
        }

        // Step 2: Find the start node of the cycle
        ListNode *slow1 = head;
        while (slow != slow1) {
            slow = slow->next;
            slow1 = slow1->next;
        }
        return slow;
    }
};
