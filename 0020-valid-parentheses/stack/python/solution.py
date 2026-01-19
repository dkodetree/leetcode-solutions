class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mapping = { "]": "[", ")": "(", "}": "{"}  # close -> open
        stack = []

        for ele in s:
            if ele in bracket_mapping.values():  # open
                stack.append(ele)
            else:                                # close
                if stack and stack[-1] == bracket_mapping[ele]:
                    stack.pop()
                else:
                    return False
        
        return not stack
