class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_p = Counter(p)
        freq_win = Counter(s[: len(p) - 1]) # initialize window except last char
        res = []
        left = 0
        
        for right in range(len(p) - 1, len(s)):
            # Add the right character to the window
            freq_win[s[right]] += 1

            # Compare current window with target (compares at most 26 letters)
            if freq_win == freq_p: 
                res.append(left)
            
            # Remove the left character to slide the window
            freq_win[s[left]] -= 1
            left += 1
        return res       
