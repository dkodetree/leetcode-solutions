class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:  
        # 1st pass: Find candidates
        majority_map = defaultdict(int) # Track up to 2 candidates
        for num in nums:
            majority_map[num] += 1
            if len(majority_map) > 2:
                new_majority_map = defaultdict(int)
                for ele, cnt in majority_map.items():
                    if cnt > 1:
                        new_majority_map[ele] = cnt - 1
                majority_map = new_majority_map
        
        # 2nd pass: Verify candidates
        res = []
        for num in majority_map:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res
