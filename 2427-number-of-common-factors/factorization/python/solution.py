import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        def get_factors(num) -> set:
            res = set()
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    res.add(i)
                    res.add(num // i)
            return res
        
        factors_a = get_factors(a)
        factors_b = get_factors(b)
        return len(factors_a & factors_b)
