import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        gcd = math.gcd(a, b)

        factors_count = 0 
        for i in range(1, int(math.sqrt(gcd)) + 1):
            if gcd % i == 0:
                factors_count += 1      # i is a factor
                if i != gcd // i:
                    factors_count += 1      # gcd // i is also a factor
        return factors_count
