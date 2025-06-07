class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums) - 1

        while left <= right:
            # Use left + (right - left) // 2 instead of (left + right) // 2 
            # to avoid overflow in languages with fixed-size integers like C++, Java, etc.
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
        
