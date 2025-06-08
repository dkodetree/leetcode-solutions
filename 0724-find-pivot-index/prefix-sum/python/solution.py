class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for idx, num in enumerate(nums):
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return idx
            left_sum += num
        return -1
