# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Dummy node to simplify edge cases
        dummy = ListNode(0, head) 
        left_prev = dummy

        # Move left_prev to the node just before "left"
        for _ in range(left - 1):
            left_prev = left_prev.next

        # Reverse sublist from left to right
        cur = left_prev.next
        prev, nxt = None, None
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        
        # Reconnect reversed sublist with the rest
        left_prev.next.next = nxt # connect tail of reversed part to the remaining list
        left_prev.next = prev # connect left_prev to the new head of reversed part
        return dummy.next
