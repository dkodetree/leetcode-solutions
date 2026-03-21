class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t, map_t_to_s = {}, {}

        for char1, char2 in zip(s, t):
            if char1 in map_s_to_t and map_s_to_t[char1] != char2:
                return False
            if char2 in map_t_to_s and map_t_to_s[char2] != char1:
                return False
            map_s_to_t[char1] = char2
            map_t_to_s[char2] = char1
            
        return True
