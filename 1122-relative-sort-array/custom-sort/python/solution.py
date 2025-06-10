class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_index_map = {ele: idx for idx, ele in enumerate(arr2)}
        
        def key(num):
            if num in arr2_index_map:
                return (0, arr2_index_map[num])
            return (1, num)
        
        return sorted(arr1, key = key)
