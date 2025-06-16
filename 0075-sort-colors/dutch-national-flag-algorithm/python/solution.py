class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        idx = 0

        while idx <= right: # Important condition
            if nums[idx] == 0:
                nums[left], nums[idx] = nums[idx], nums[left] # Swap with left
                left += 1
                idx += 1
            elif nums[idx] == 1: # No swap needed for 1
                idx += 1
            else:
                nums[idx], nums[right] = nums[right], nums[idx] # Swap with right
                right -= 1
