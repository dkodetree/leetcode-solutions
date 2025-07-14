# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        cur = head
        binary = 0
        while cur:
            binary = binary * 2  + cur.val
            cur = cur.next
        return binary
