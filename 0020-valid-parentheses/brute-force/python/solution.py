class Solution:
    def isValid(self, s: str) -> bool:
        cur_str = s
        while "()" in cur_str or "{}" in cur_str or "[]" in cur_str:
            cur_str = cur_str.replace("()", "")
            cur_str = cur_str.replace("{}", "")
            cur_str = cur_str.replace("[]", "")
        return cur_str == ""
