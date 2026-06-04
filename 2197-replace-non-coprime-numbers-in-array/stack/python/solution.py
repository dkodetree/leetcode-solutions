class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)

            while len(stack) >= 2:
                num1, num2 = stack[-1], stack[-2]

                hcf = math.gcd(num1, num2)
                if hcf == 1: # co-prime, no merging needed
                    break

                lcm = num1 * num2 // hcf
                stack.pop()
                stack.pop()
                stack.append(lcm)
                
        return stack
