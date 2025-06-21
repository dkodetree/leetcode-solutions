class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mapping = { "]": "[", ")": "(", "}": "{"}  # close -> open
        stack = []

        for ch in s:
            if ch in bracket_mapping.values():  # open
                stack.append(ch)
            else:   # close
                if stack and stack[-1] == bracket_mapping[ch]:
                    stack.pop()
                else:
                    return False
        
        return not stack
