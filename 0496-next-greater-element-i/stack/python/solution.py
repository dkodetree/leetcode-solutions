class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = []  # Monotonic Decreasing Stack (Left to Right Scan)
        nums1_idx_map = {num: idx for idx, num in enumerate(nums1)}

        for idx, num in enumerate(nums2):
            while stack and stack[-1] < num:
                value = stack.pop()
                res_idx = nums1_idx_map[value] 
                res[res_idx] = num
            if num in nums1_idx_map:
                stack.append(num)
        return res
