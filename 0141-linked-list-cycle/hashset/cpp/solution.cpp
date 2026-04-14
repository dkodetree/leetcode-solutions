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
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> visited;
        ListNode* cur = head;

        while (cur != nullptr) {
            if (visited.find(cur) != visited.end()) {
                return true;
            }
            visited.insert(cur);
            cur = cur->next;
        }
        return false;
    }
};
