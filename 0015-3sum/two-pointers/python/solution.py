class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)

        res = []
        for i in range(length):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue    

            left, right = i + 1, length - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if cur_sum < 0:
                    # Move left and skip duplicates for second number
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif cur_sum > 0:
                    # Move right and skip duplicates for the third number
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]]) 

                    # Move both pointers and skip duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return res
