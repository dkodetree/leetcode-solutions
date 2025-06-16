class Solution:
    def fib(self, n: int) -> int:
        dp = {}     # Dictionary for Tabulation
        
        for i in range(n + 1):
            if i <= 1:
                dp[i] = i
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
    
        return dp[n]
