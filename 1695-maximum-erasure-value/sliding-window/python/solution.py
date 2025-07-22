class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = set()      # current window containing unique elements
        current_sum = 0     # sum of the current window
        max_sum = 0         # best sum found so far

        left = 0
        for right in range(len(nums)):
            # Shrink window if nums[right] already exists in window
            while nums[right] in window:
                window.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            # Add nums[right] to window
            window.add(nums[right])
            current_sum += nums[right]

            # Update the best erasure value
            max_sum = max(current_sum, max_sum)

        return max_sum
