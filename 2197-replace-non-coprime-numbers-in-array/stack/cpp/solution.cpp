class Solution {
public:
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        vector<int> stack;
        for (int num : nums) {
            stack.push_back(num);

            while (stack.size() >= 2) {
                int num1 = stack.back();
                int num2 = stack[stack.size() - 2];

                if (gcd(num1, num2) == 1) { // co-prime, no merging needed
                    break;
                }

                long long lowest_common_multiple = lcm<long long>(num1, num2);
                stack.pop_back();
                stack.pop_back();
                stack.push_back(static_cast<int>(lowest_common_multiple));
            }
        }
        return stack;
    }
};
