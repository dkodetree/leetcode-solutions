class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur_majority_ele, count = None, 0
        for num in nums:
            if count == 0:
                cur_majority_ele, count = num, 1
            elif cur_majority_ele == num:
                count += 1
            else:
                count -= 1
        return cur_majority_ele
