class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = collections.Counter(s)

        for mid in s: # atmost n
            right[mid] -= 1
            for outer in left: # atmost 26
                if right[outer] > 0:
                    res.add((outer, mid))
            left.add(mid)
        
        return len(res)
