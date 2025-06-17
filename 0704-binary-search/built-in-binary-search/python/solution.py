import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)  # Leftmost position to insert target while maintaining order
        if index < len(nums) and nums[index] == target:  # Confirm that the target exists at this index
            return index
        return -1
