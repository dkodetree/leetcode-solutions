class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = collections.defaultdict(int)
        majority_element, highest_count = 0, 0
        
        for num in nums:
            freq_map[num] += 1
            if freq_map[num] > highest_count:
                majority_element = num
                highest_count = freq_map[num]
        return majority_element
