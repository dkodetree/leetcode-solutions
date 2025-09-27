from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = Counter(nums)
        most_common_list = count_map.most_common(1)
        return most_common_list[0][0]
