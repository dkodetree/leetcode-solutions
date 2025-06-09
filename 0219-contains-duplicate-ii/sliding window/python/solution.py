class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for num in nums:
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[left])
                left += 1
        return False
