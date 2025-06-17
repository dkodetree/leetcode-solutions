class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = [char.lower() for char in s if char.isalnum()]
        return valid_chars == valid_chars[::-1]
