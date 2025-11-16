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
    void deleteNode(ListNode* node) {
        ListNode* temp = node->next;   // Preserve pointer to next node
        node->val = temp->val;         // Copy next node's value
        node->next = temp->next;       // Skip next node
        delete temp;                   // Free memory
    }
};
