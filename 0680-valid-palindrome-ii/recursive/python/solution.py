class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right, deletion_used):
            if left >= right:
                return True
            if s[left] == s[right]:
                return is_palindrome(left + 1, right - 1, deletion_used) 
            if deletion_used:
                return False
            return is_palindrome(left + 1, right, True) or is_palindrome(left, right - 1, True)
            
        return is_palindrome(0, len(s) - 1, False)
