class Solution:
    def fib(self, n: int) -> int:
        dp = {}     # Dictionary for Memoization
        
        def fib_helper(num):
            if num <= 1:
                return num
            if num in dp:
                return dp[num]
            dp[num] = fib_helper(num - 1) + fib_helper(num - 2)
            return dp[num]

        return fib_helper(n)
