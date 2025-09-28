class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:  
        freq_map = collections.defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        res = []
        n = len(nums)
        for ele, cnt in freq_map.items():
            if cnt > n // 3:
                res.append(ele)
        return res
