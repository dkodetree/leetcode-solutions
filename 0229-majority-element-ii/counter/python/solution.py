class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:  
        count_map = collections.Counter(nums)
        n = len(nums)
        res = []
        for num, cnt in count_map.most_common(2):
            if cnt > n // 3:
                res.append(num)
        return res
