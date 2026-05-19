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
        unordered_set<ListNode*> visited;
        ListNode* cur = head;
        while (cur) {
            if (visited.find(cur) != visited.end()) {
                return cur;     // Cycle entry found
            }
            visited.insert(cur);
            cur = cur->next;
        }
        return nullptr;        // No Cycle 
    }
};
