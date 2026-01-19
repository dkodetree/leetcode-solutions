class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []  # Monotonic Increasing Stack
        deleted_cnt = 0
        for digit in num:
            while stack and stack[-1] > digit and deleted_cnt < k:
                stack.pop()
                deleted_cnt += 1
            stack.append(digit)
        
        while stack and deleted_cnt < k:
            stack.pop()
            deleted_cnt += 1
        
        res = "".join(stack)
        return res.lstrip("0") or "0" # Remove leading zeros
