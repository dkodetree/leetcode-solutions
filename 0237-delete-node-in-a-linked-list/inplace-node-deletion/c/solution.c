/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    struct ListNode* temp = node->next;   // Preserve pointer to next node
    node->val = temp->val;                // Copy next node's value
    node->next = temp->next;              // Skip next node
    free(temp);                           // Free memory of the skipped node
}
