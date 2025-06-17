import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)     # Builds entire min-heap from list (not just "heapifying" one node)
        result = []                
        while nums:
            result.append(heapq.heappop(nums))  # Fetches the minimum element each time
        return result           # Returns a new sorted list (Not in-place)
