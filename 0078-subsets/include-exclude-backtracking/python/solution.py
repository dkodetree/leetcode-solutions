class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, subset):
            if idx >= len(nums):
                res.append(subset.copy())
                return
                
            # Include the current element
            subset.append(nums[idx])    # Choose
            backtrack(idx + 1, subset)  # Explore
            subset.pop()                # Undo (Backtrack)

            # Exclude the current element
            backtrack(idx + 1, subset)
        
        backtrack(0, [])
        return res
