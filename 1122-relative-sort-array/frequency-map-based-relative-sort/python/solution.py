class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq_map = collections.Counter(arr1)
        res = []

        # Add elements in the order defined by arr2, and remove from the frequency map
        for num in arr2:    
            num_cnt = freq_map.pop(num, 0)
            res.extend([num] * num_cnt)
        
        # Add remaining elements in ascending order
        for key in sorted(freq_map):    
            cnt = freq_map[key]
            res.extend([key] * cnt)
        return res
