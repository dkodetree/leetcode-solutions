class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def backtrack(cur_idx):
            # Append a copy of current subset
            res.append(subset.copy())

            # Iterate through the remaining elements
            for idx in range(cur_idx, len(nums)):
                subset.append(nums[idx])    # Choose
                backtrack(idx + 1)          # Explore
                subset.pop()                # Undo

        backtrack(0)
        return res
