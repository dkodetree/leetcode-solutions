import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python's heapq module only supports min-heaps by default. So, convert the list into a max-heap by negating the values.
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first_stone = -heapq.heappop(max_heap)
            second_stone = -heapq.heappop(max_heap)
            if first_stone != second_stone:
                heapq.heappush(max_heap, -(first_stone - second_stone))
        return -max_heap[0] if max_heap else 0
