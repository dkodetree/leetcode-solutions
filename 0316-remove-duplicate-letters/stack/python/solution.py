class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        last_occ = {}

        for idx, ele in enumerate(s):
            last_occ[ele] = idx

        stack = []
        for idx, ele in enumerate(s):
            if ele in seen:
                continue
            while stack and stack[-1] > ele and last_occ[stack[-1]] > idx:
                removed_ele = stack.pop() 
                seen.remove(removed_ele) # Remove from seen set, as it's not in stack anymore
            stack.append(ele)
            seen.add(ele)
        return "".join(stack)
