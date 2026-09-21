/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        // Dummy node to simplify edge cases
        ListNode* dummy = new ListNode(0, head); // dummy on heap
        ListNode* left_prev = dummy;

        // Move left_prev to the node just before "left"
        for (int i = 0; i < left - 1; i++) {
            left_prev = left_prev->next;
        }

        // Reverse sublist from left to right
        ListNode* cur = left_prev->next;
        ListNode* prev = nullptr;
        ListNode* nxt = nullptr;
        for (int i = 0; i < right - left + 1; i++) {
            nxt = cur->next;
            cur->next = prev;
            prev = cur;
            cur = nxt;
        }

        // Reconnect reversed sublist with the rest
        left_prev->next->next = nxt; // connect tail of reversed part to the remaining list
        left_prev->next = prev;      // connect left_prev to the new head of reversed part

        ListNode* new_head = dummy->next;
        delete dummy; // clean up the memory allocated for dummy node
        return new_head;
    }
};
