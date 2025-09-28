class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:  
        freq_map = collections.defaultdict(int)
        n = len(nums)
        res = set()
        for num in nums:
            freq_map[num] += 1
            if freq_map[num] > n // 3:
                res.add(num)
        return list(res)
