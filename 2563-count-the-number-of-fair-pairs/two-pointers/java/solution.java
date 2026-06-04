class Solution {
    public long countFairPairs(int[] nums, int lower, int upper) {
        Arrays.sort(nums);
        return countPairs(nums, upper) - countPairs(nums, lower - 1);
    }

    // Helper to count pairs with sum less than or equal to upperBound
    private long countPairs(int[] nums, int upperBound) {
        long count = 0;
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int pairSum = nums[left] + nums[right];
            if (pairSum <= upperBound) {
                count += (right - left);
                left++;
            } else {
                right--;
            }
        }
        return count;
    }
    
}
