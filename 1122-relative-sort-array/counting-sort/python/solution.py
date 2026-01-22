class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_num = max(arr1)
        count = [0] * (max_num + 1)
        for num in arr1:
            count[num] += 1
        
        res = []
        for num in arr2:
            res.extend([num] * count[num])
            count[num] = 0
        
        for num in range(max_num + 1):
            res.extend([num] * count[num])
        return res
