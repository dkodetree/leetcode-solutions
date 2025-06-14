class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(cur_idx, cur_subset):
            # Append a copy of current subset
            res.append(cur_subset.copy())

            # Iterate through the remaining elements
            for idx in range(cur_idx, len(nums)):
                cur_subset.append(nums[idx])        # Choose
                backtrack(idx + 1, cur_subset)      # Explore
                cur_subset.pop()                    # Undo

        backtrack(0, [])
        return res
