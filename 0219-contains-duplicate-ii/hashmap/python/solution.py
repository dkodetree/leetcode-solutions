class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for idx, num in enumerate(nums):
            if num in index_map and idx - index_map[num] <= k:
                return True
            index_map[num] = idx
        return False
