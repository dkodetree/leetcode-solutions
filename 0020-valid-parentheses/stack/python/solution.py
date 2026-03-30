class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = { "]": "[", ")": "(", "}": "{"}  # close -> open
        open_bracket_stack = []

        for ele in s:
            if ele in bracket_map:      # close                        
                if open_bracket_stack and open_bracket_stack[-1] == bracket_map[ele]:
                    open_bracket_stack.pop()
                else:
                    return False
            else:
                open_bracket_stack.append(ele)       # open

        return not open_bracket_stack
