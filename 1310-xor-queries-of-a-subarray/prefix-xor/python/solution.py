class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        length = len(arr)
        prefix_xor = [0] * (length + 1)
        
        for idx, ele in enumerate(arr):
            prefix_xor[idx + 1] = prefix_xor[idx] ^ ele
        
        result = []
        for left, right in queries:
            result.append(prefix_xor[right + 1] ^ prefix_xor[left])
        
        return result
