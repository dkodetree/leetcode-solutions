class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def count_pairs(upper_bound) -> int: #count pairs with sum less than or equal to upper_bound
            left, right = 0, len(nums) - 1
            cnt = 0
            while left < right:
                pair_sum = nums[left] + nums[right]
                if pair_sum <= upper_bound:
                    cnt += right - left
                    left += 1
                else:
                    right -= 1
            return cnt

        return count_pairs(upper) - count_pairs(lower - 1)
