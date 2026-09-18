class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for num in nums_set:
            if num - 1 not in nums_set: # ie. num becomes start of a sequence
                length = 1
                while num + length in nums_set:
                    length += 1
                max_length = max(max_length, length)
        return max_length
