class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def backtrack(idx):
            if idx >= len(nums):
                res.append(subset.copy())
                return

            # Include
            subset.append(nums[idx])    # Choose
            backtrack(idx + 1)          # Explore
            subset.pop()                # Undo (Backtrack)

            # Exclude
            backtrack(idx + 1)
        
        backtrack(0)
        return res
