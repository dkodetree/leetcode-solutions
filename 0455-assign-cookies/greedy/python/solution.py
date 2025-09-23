class Solution:
    def findContentChildren(self, greed_factors: List[int], cookie_sizes: List[int]) -> int:
        greed_factors.sort()
        cookie_sizes.sort()

        child_idx = 0 
        cookie_idx = 0 

        while child_idx < len(greed_factors) and cookie_idx < len(cookie_sizes):
            # Give cookie if it satisfies the child's greed
            if greed_factors[child_idx] <= cookie_sizes[cookie_idx]:
                child_idx += 1
            cookie_idx += 1
        return child_idx
