class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = set()
        for i in range(length):
            # Skip duplicate first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            seen = set()
            for j in range(i + 1, length):
                target = - (nums[i] + nums[j])
                if target in seen:
                    res.add((nums[i], nums[j], target))
                seen.add(nums[j])
        return [[x, y, z] for x, y, z in res]
