class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        length = len(nums)

        res = []
        for i in range(length):
            # Its impossible to get a triplet summing to 0 after the first number becomes +ve
            if nums[i] > 0: 
                break

            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue    

            left, right = i + 1, length - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if cur_sum < 0:
                    left += 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]]) # Found a valid triplet

                    # Move both pointers and skip duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res
