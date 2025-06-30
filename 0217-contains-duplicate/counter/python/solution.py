class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = collections.Counter(nums)
        for cnt in freq.values():
            if cnt > 1:
                return True
        return False
