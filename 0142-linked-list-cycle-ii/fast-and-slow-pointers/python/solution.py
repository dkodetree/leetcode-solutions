# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Detect the Cycle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break   # cycle detected  
        else:
            return None

        # Step 2: Find the start node of the Cycle
        slow1 = head
        while slow != slow1:
            slow = slow.next
            slow1 = slow1.next
        return slow
