from sortedcontainers import SortedSet

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        window = SortedSet() # Maintain a sorted sliding window

        left = 0
        for num in nums:
            # Find the smallest number in the window that is ≥ (num - valueDiff), as a potential nearby almost duplicate
            pos = window.bisect_left(num - valueDiff) 

            # Check if that number is within valueDiff of current num
            if pos < len(window) and abs(num - window[pos]) <= valueDiff:
                return True

            window.add(num)
            # Ensure window size does not exceed indexDiff
            if len(window) > indexDiff:
                window.remove(nums[left])
                left += 1

        return False
