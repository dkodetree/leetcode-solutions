class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:      

        heap_size = 0
        n = len(nums)      

        def max_heapify(idx):       # O(log n)
            nonlocal heap_size
            largest = idx
            left, right = 2 * idx + 1, 2 * idx + 2
            
            if left < heap_size and nums[left] > nums[largest]:
                largest = left   
            if right < heap_size and nums[right] > nums[largest]:
                largest = right
            
            if largest != idx:
                nums[largest], nums[idx] = nums[idx], nums[largest]   # swap
                max_heapify(largest)

        def build_heap():           # O(n)
            nonlocal heap_size
            heap_size = n
            for idx in range(len(nums) // 2 - 1, -1 , -1):
                max_heapify(idx)
        
        def heap_sort():            # O(n log n)
            nonlocal heap_size
            build_heap()                        
            for idx in range(n - 1, 0, -1):   # from n-1 down to 1 (leaving index 0, which ends up in correct place)
                nums[0], nums[idx] = nums[idx], nums[0]
                heap_size -= 1
                max_heapify(0)         

        heap_sort() 
        return nums
