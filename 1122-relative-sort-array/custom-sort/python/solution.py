class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {ele: idx for idx, ele in enumerate(arr2)}
        
        def relative_key(num):
            if num in order:
                return (0, order[num])
            return (1, num)
        
        return sorted(arr1, key=relative_key)
