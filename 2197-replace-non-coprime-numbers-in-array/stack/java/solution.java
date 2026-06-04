class Solution {
    public List<Integer> replaceNonCoprimes(int[] nums) {
        List<Integer> stack = new ArrayList<>();
        for (int num : nums) {
            stack.add(num);

            while (stack.size() >= 2) {
                int num1 = stack.get(stack.size() - 1);
                int num2 = stack.get(stack.size() - 2);
                
                int hcf = gcd(num1, num2);
                if (hcf == 1) { // co-prime, no merging needed
                    break;
                }

                long lcm = ((long) num1 * num2) / hcf;
                stack.remove(stack.size() - 1);
                stack.remove(stack.size() - 1);
                stack.add((int) lcm);
            }
        }
        return stack;
    }
    
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
