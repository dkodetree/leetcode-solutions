class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)

            while len(stack) >= 2:
                a, b = stack[-1], stack[-2]
                hcf = math.gcd(a, b)
                if hcf == 1: # co-prime
                    break
                lcm = a * b // hcf
                stack.pop()
                stack.pop()
                stack.append(lcm)
        return stack
