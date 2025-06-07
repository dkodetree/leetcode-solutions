class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # num : idx
        for idx, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], idx]
            seen[num] = idx
        return []
