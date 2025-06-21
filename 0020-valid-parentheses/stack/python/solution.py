class Solution:
    def isValid(self, s: str) -> bool:
        brackets_mapping = { ")" : "(", "]" : "[", "}" : "{" } # close -> open
        stack = []
    
        for ch in s:
            if ch in brackets_mapping.values():
                stack.append(ch)
            elif ch in brackets_mapping and stack and stack[-1] == brackets_mapping[ch]: # stack[-1] is top
                stack.pop()
            else:   
                return False

        return not stack
