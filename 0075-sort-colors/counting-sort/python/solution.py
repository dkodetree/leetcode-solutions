from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = collections.Counter(nums)
        idx = 0
        for color in range(3):
            while(freq[color]):
                nums[idx] = color
                freq[color] -= 1
                idx += 1
