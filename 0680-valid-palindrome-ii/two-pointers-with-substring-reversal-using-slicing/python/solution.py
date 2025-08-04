class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            return s[left:right + 1] == s[left:right + 1][::-1]
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left, right - 1) or is_palindrome(left + 1, right)
            left += 1
            right -= 1
        return True
