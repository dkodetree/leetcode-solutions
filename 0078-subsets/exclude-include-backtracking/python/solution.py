class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, subset):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            
            # Exclude the current element
            backtrack(idx + 1, subset)

            # Include the current element
            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            
            # Backtrack: Undo the include decision (Important step)
            subset.pop()
            
        backtrack(0, [])
        return res
