class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find intersection point
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 1: Find entrance to the cycle
        slow1 = 0
        while slow != slow1:
            slow = nums[slow]
            slow1 = nums[slow1]
        return slow
