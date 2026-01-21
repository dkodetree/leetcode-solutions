class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {ele: idx for idx, ele in enumerate(arr2)}        
        return sorted(arr1, key=lambda x: (order.get(x, float("inf")), x))
